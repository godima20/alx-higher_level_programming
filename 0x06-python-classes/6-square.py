#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square class defined by geometric shap

        Attributes:
            size (int): size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of the side of the square
            position(tuple): position of square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """
        set square square area

        Return:
            the current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter of size

        Return:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size

        Args:
            value (int): size of side of square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print a square from the size using ##

        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self._position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    @property
    def position(self):
        """
        get position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter of position
        Args:
            value(tuple): position of the square in 2D space
        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
