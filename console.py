#!/usr/bin/python3

"""Definition of a command interpreter class."""

import cmd
import json
import os.path
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter console class."""

    prompt = '(hbnb) '
    __available_classes = {"BaseModel", "User", "State", "City", "Amenity"
                           "Place", "Review"}
    #  __funcs = {"create", "show", "all", "destroy", "update", "count"}

    def do_EOF(self, arg):
        """EOF command to exit the program.

        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program.

        """
        return True

    def emptyline(self):
        pass

    def default(self, arg):
        """Handles alternative usage."""
        a = splitter(arg)
        if a[0] not in self.__available_classes:
            print(f'*** Unknown syntax: {a[0]}')
            return
        else:
            if not a[-2]:
                a = a[1:2] + a[0:1] + a[2:-2]
            else:
                a = a[1:2] + a[0:1] + a[2:-1]
            str_arg = ' '.join(a)
            HBNBCommand().onecmd(str_arg)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) \
                and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        a = arg.strip().split()

        b = cid_exist(a[0], '00')

        if a[0] not in HBNBCommand.__available_classes:
            print("** class doesn't exist **")
            return

        new_cls = eval(a[0])()
        new_cls.save()
        print(new_cls.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based \
                on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return False

        a = shlex.split(arg)

        if len(a) < 2:
            print("** instance id missing **")
            return False

        b = cid_exist(a[0], a[1])

        if not b:
            print("** class doesn't exist **")
            return False

        if len(b) < 3:
            print("** no instance found **")
            return False

        print((b[2].all())[b[1]])

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""

        fs = FileStorage()
        fs.reload()
        fs_obj = fs.all()
        if arg:
            a = shlex.split(arg)
            k = [str(val) for key, val in fs_obj.items()
                 if a[0] in key.split('.')]
            if not k:
                print('0')
            else:
                print(len(k))
        else:
            print('0')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the \
                change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return False

        a = shlex.split(arg)

        if len(a) < 2:
            print("** instance id missing **")
            return False

        b = cid_exist(a[0], a[1])

        if not b:
            print("** class doesn't exist **")
            return False

        if len(b) < 3:
            print("** no instance found **")
            return False

        b_obj = b[2].all()
        #  b[2] is a FileStorage object retured from cid_exist function
        #  b[1] is a key in FileStorage.__objects corresponding to object ID
        del b_obj[b[1]]
        b[2].save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or \
                not on the class name.
        """
        fs = FileStorage()
        fs.reload()
        fs_obj = fs.all()
        if arg:
            a = shlex.split(arg)
            k = [str(val) for key, val in fs_obj.items()
                 if a[0] in key.split('.')]
            if not k:
                print("** class doesn't exist **")
            else:
                print(k)
        else:
            b = [str(val) for val in fs_obj.values()]
            print(b)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or \
            updating attribute and save the change into the JSON file.
        usage: update <class name> <id> <attribute name> "<attribute value>".
        """

        if not arg:
            print("** class name missing **")
            return False

        a = shlex.split(arg)

        dct_o_patt = r"^\{\w+\:?\w+\:?$"
        dct_c_patt = r"^\w+\:?\w+\:?\}$"
        mc = re.match(dct_c_patt, a[-1])
        mo = re.match(dct_o_patt, a[2])

        if mc and mo:
            p_dct = r"\{|\}|\:|,"
            p_str = re.split(p_dct, ','.join(a[2:]))
            a = a[0:2] + p_str[1:-1]

        attr = a[2:]
        if len(a) < 2:
            print("** instance id missing **")
            return False

        if len(a) < 3:
            print("** attribute name missing **")
            return False

        if len(attr) % 2 != 0:
            print("** value missing **")
            return False

        b = cid_exist(a[0], a[1])
        if not b:
            print("** class doesn't exist **")
            return False

        if len(b) < 3:
            print("** no instance found **")
            return False

        fs = b[2]
        fs_obj = fs.all()
        bmodel = fs_obj[b[1]]

        int_patt = r"^\d+$"
        flt_patt = r"^\d+(\.){1}\d+$"
        for k in range(0, len(attr), 2):  # list: [cls, id, k1, v1, k2, v2..}
            v = k + 1
            val = attr[v]
            if not val:
                print("** value missing **")
                return
            mi = re.match(int_patt, val)
            mf = re.match(flt_patt, val)
            if mi:
                val = int(val)
            elif mf:
                val = float(val)
            else:
                val = str(val)
            setattr(bmodel, attr[k], val)
        bmodel.save()

    def postloop(self):
        """prints a newline after EOF."""
        print('')


def cid_exist(cls, oid):
    """Returns list of class name or/and obj from json file."""
    k = []
    fs = FileStorage()
    fs.reload()
    fs_obj = fs.all()
    for key in fs_obj.keys():
        s = key.split('.')
        if cls in s and cls not in k:
            k.append(s[0])
        if oid in s:
            k.append(key)
            k.append(fs)
            return k
    return k


def splitter(arg):
    """splits argument based on pattern"""
    pattern1 = r'\w+( \"?(\w+\-*)+\"?)+'
    pattern2 = r'\w+\.\S+'
    match1 = re.match(pattern1, arg)
    match2 = re.match(pattern2, arg)
    if match1 and match1.group() is arg:
        return shlex.split(arg)
    elif match2:
        pattern = r"(?<!\d)\.|,|\(|\)"
        result = re.split(pattern, arg)
        res = []
        for i in result:
            ret = ''.join(shlex.split(i))
            res.append(ret.strip())
        return res
    else:
        return [arg]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
