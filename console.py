#!/usr/bin/python3
"""
    Console module
"""

import cmd
from models.base_model import BaseModel
from models.user import User
import json

class HBNBCommand(cmd.Cmd):
    """ Console prompt  """
    prompt = "(hbnb) "

    """ --Classes """
    __classes = ['BaseModel', 'User']


    """ --Commands """
    __commands = ['create', 'show', 'destroy', 'all', 'update']


    def emptyline(self):
        """do nothing when empty"""
        pass

    def do_quit(self, arg):
        """exit program when arg is quit"""
        raise SystemExit

    def do_EOF(self, arg):
        """exits program when arg is EOF"""
        raise SystemExit
    
    def do_create(self, prmArg):
        """
        creates a new instance of BaseModel, 
        saves it to the JSON file and prints the id.
        """
        if not prmArg:
            raise ValueError("** class name missing **")
        elif prmArg not in self.__classes:
            raise ValueError("** class doesn't exist **")
        else:
            model_classes = {'BaseModel': BaseModel, 'User': User}
            my_model = model_classes[prmArg]()
            print(my_model.id)
            storage.save()    

    def do_show(self, prmArg):
        """ prints the string representation of an instance based on the class name and id """

        if not prmArg:
            raise ValueError(" ** class name missing **")
            return

        prmArgs = prmArg.split(' ')

        if prmArgs[0] not in self.__classses:
            raise ValueError("** class doesn't exist **")
        elif len(prmArgs) == 1:
            raise ValueError("** instance id missing **")
        else:
            dict_obj = storage.all()
            key = "{}.{}".format(prmArgs[0], prmArgs[1])
            if key not in dict_obj:
                raise ValueError("** no instance found **")

            print(dict_obj[key])

    def do_destroy(self, prmArgs):
        """ deletes an instance based on the class name ad id """
        if not prmArgs:
            raise ValueError("** class name missing **")

        args = prmArgs.split(' ')
        
        if args[0] not in self.__classes:
            raise ValueError("** class doesn't exist **")
        elif len(args) == 1:
            raise ValueError("** instance id missing **")
        else:
            dict_obj = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dict_obj:
                raise ValueError("** no instance found **")

            del dict_obj[key]
            storage.save()

    def do_all(self, prmArgs):
        """ prints all string representarion of all instances based or not on the class name """
        args = prmArgs.split(' ')
        
        if args and args[0] not in self.__classes:
            raise ValueError("** class doesn't exist **")
        
        dict = storage.all()
        list = []

        for key, value in dict.items():
            obj_name = value.__class__.__name__
            if(not args or args[0] or obj_name == args[0]):
                list += [value.__str__()]

        print(list)

    def do_update(self, prmArg):
        """ updates an instance based on the class name and id by adding or updating attribute(save the change into JSONfile) """

        if not prmArg:
            raise ValueError("** class name missing **")

        args = prmArg.split(' ')

        className, command, attribute, value = args

        if args[0] not in self.__classes:
            raise ValueError("** class doesn't exist **")
        if len(args) == 1:
            raise ValueError("** instance id missing **")

        dict_obj = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in dict_obj:
            raise ValueError("** no instance found **")
        obj_value = dict_obj[key]

        if len(args) == 2:
            raise ValueError("** attribute name is missing **")

        if len(args) == 3:
            raise ValueError("** value is missing **")

        if attribute not in ("id", "create_at", "updated_at"):
            setattr(obj_value, attribute, self.__type(value))

            storage.save()

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF(end of file) command to exit the program\n")
    
    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.\n")

    def help_show(self):
        print("Prints the string representation of an instance based on the classname and id.\n")  

    def help_destroy(self):
        print("Deletes an instance based on the class name and id(save the change into the JSON file).\n")

    def help_all(self):
        print("Prints all the string representation of all instances based or not on the class name,\n")

    def help_update(self):
        print("Updates an instance based on the class name and id by \ adding or updating attribute (save the change into the JSON file).\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()