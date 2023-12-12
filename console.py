#!/usr/bin/python3
"""Define a cmd class"""
import cmd


class HBNBCommand(cmd.Cmd):

    """ Console for the hbnb app"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, line):
        """
        Handles the 'EOF' command to exit the console

        PARAMETERS:
        --self: An instance of the console processor
        --line: The input from the user containing the 'EOF'

        RETURNS:
        --True: Signals the console to quit
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
