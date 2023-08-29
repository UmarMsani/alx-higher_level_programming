#!/usr/bin/python3

"""This module defines a Square class."""


class Square:
    """This class represents a square with size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (number, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (number): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square's area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if the area of one square is less than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of one square is less than or equal to another."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if the area of one square is greater than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of one square is greater than or equal to another."""
        return self.area() >= other.area()
