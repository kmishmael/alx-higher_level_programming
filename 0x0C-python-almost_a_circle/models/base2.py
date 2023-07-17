#!/usr/bin/usr
"""Definition of base class"""


class Base:
    """Base class definition"""
    __nb_objects = 0
    def __init__(self, id=None):
        """constructor"""
        if id != None:
            self.id = id
        else:
            self.__nb_objects = self.__nb_objects + 1
            self.id = self.__nb_objects