from cmd import Cmd

import rabbitmq
from background_job import initiate_background_tasks

import asyncio
from threading import Thread

class CLIApp(Cmd):
    prompt = '>>> '
    def do_greet(self, line):
        print("Hello, %s" % line)

    def do_exit(self, line):
        return True

    def do_publish(self, line):
        rabbitmq.publish_message_my_queue(line)


if __name__ == '__main__':
    # Set up the asyncio event loop in a separate thread
    loop = asyncio.new_event_loop()
    t = Thread(target=loop.run_forever, daemon=True)
    t.start()

    # Initiate background tasks (RabbitMQ listener)
    initiate_background_tasks(loop)

    # Run the command line app
    CLIApp().cmdloop()

    # Clean up the event loop
    loop.call_soon_threadsafe(loop.stop)
    t.join()
