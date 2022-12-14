#!/usr/bin/python3
"""
A student class that defines a Studen (module)
"""


class Student():
    """
        A student class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
            INIT
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation
            of a student instance
        """
        return(self.__dict__)
