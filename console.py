#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    obj_dict = models.storage._FileStorage__objects
    cls_dict = {"BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}

    def do_EOF(self, line):
        """Command to exit the Interpreter typing EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty line + ENTER execute anything"""
        pass

    def do_create(self, arg):
        """A method that creates an instance of a class."""
        if not arg:
            print("** class name missing **")
        elif arg in self.cls_dict:
            name = self.cls_dict[arg]
            new = name()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance with the class name and id"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] in self.cls_dict:
            if len(args) != 2:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) in HBNBCommand.obj_dict:
                del(HBNBCommand.obj_dict["{}.{}".format(args[0], args[1])])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
        models.storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in self.cls_dict:
            print("** class doesn't exist **")
        else:
            instance = args[0] + '.' + args[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print('** no instance found **')

    def do_all(self, line):
        """ Prints all string representation of all instances based or not on the class name """
        args = shlex.split(line)
        if len(args) == 0:
            obj_list = []
            for key in models.storage.all():
                obj_list.append(str(models.storage.all()[key]))
            print(obj_list)
        elif args[0] in self.cls_dict:
            obj_list = []
            for key in models.storage.all():
                if args[0] in key:
                   obj_list.append(str(models.storage.all()[key]))
            print(obj_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
