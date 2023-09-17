#!/usr/bin/python3
"""This defines a square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square (default is 0).
            y (int): y-coordinate of the square (default is 0).
            id (int): Optional id value (default is None).
        """
        super().__init__(size, size, x, y, id)  # Call superclass constructor with size as width and height

    @property
    def size(self):
        """
        Getter for size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute. Assigns the value to both width and height.

        Args:
            value (int): The size to be assigned.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes with provided arguments and keyword arguments.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.

        Returns:
            dict: The dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: The string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
