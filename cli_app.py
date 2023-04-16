from cmd import Cmd


class CLIApp(Cmd):

    def do_greet(self, line):
        print("Hello, %s" % line)

    def do_exit(self, line):
        return True


if __name__ == '__main__':
    CLIApp().cmdloop()
