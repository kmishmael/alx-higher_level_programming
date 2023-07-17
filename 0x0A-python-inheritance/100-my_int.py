#!/usr/bin/python3

"""Definition of MyInt class"""


class MyInt(int):
    """class defintion"""

    def __eq__(self, value):
        """override == operator"""
        return self.real != value

    def __ne__(self, value):
        """override != operator"""
        return self.real == value
