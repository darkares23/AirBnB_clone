#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Command to exit the Interpreter typing EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty line + ENTER execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
