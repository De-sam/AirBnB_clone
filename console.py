#!/usr/bin/python3
"""Console module"""

import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from datetime import datetime

all_classes = [
    "BaseModel"]


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args or args[0] not in storage.all():
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            print(instances.get(key, "** no instance found **"))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args or args[0] not in storage.all():
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            del instances[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of the instances
        depending on the class name"""
        arg_list = split(arg)
        objects = storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in all_classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args or args[0] not in storage.all():
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            obj = instances[key]
            setattr(obj, args[2], args[3])
            obj.updated_at = datetime.now()
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
