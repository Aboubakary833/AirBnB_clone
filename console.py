#!/usr/bin/python3
"""The Console"""

import cmd


class AirBnBCmd(cmd.Cmd):
    """AirBnBCmd class"""
    prompt = "(hbnb) help"


if __name__ == '__main__':
    """infinite loop"""
    AirBnBCmd().cmdloop()
