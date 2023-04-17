import asyncio

from rabbitmq import setup_rabbitmq


def initiate_background_tasks(loop):
    """Initiate the background tasks."""
    try:
        # Schedule the RabbitMQ setup function to run in the event loop
        asyncio.run_coroutine_threadsafe(setup_rabbitmq(loop), loop)
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    """Main function to run the script

    This function will run the script and initiate the background tasks."""
    initiate_background_tasks()
