#!/usr/bin/usr
"""Definition of base class"""


class Base:
    """
    Base model

    This represents the `base` of all other classes in the project.

    Private class attributes:
        __nb_objects (int): base model live instances
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        The constructor
        
        Args:
            id (int): unique id of an instance
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects