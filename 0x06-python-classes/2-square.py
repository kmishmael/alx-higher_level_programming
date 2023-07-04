#!/usr/bin/python3

"Represents a sqaure"


class Square:
    """The square"""
    def __init__(self, size=0):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
