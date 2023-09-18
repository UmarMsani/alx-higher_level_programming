#!/usr/bin/python3
"""This defines base model class"""
import json
import csv
import os.path


class Base:
    """
    Base class for managing id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): Optional id value (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(file_name, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        import json

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            instance: An instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            return None

        dummy.update(**dictionary)  # Apply the real values using update method
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: List of instances.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dic) for dic in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def to_csv_string(list_dictionaries):
        """
        Convert a list of dictionaries to a CSV string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: CSV string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ""

        csv_string = ""
        for dic in list_dictionaries:
            values = [str(val) for val in dic.values()]
            csv_string += ",".join(values) + "\n"

        return csv_string

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".csv"
        csv_string = cls.to_csv_string([obj.to_dictionary() for obj in list_objs])

        with open(file_name, 'w') as file:
            file.write(csv_string)

    @staticmethod
    def from_csv_string(csv_string):
        """
        Convert a CSV string to a list of dictionaries.

        Args:
            csv_string (str): CSV string.

        Returns:
            list: List of dictionaries.
        """
        if csv_string is None or csv_string == "":
            return []

        lines = csv_string.strip().split("\n")
        dictionaries = []
        for line in lines:
            values = line.split(",")
            d = {k: int(v) for k, v in zip(["id", "width", "height", "x", "y"], values)}
            dictionaries.append(d)

        return dictionaries

    @classmethod
    def load_from_file_csv(cls):
        """
        Load instances from a CSV file and return a list of instances.

        Returns:
            list: List of instances.
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, 'r') as file:
                csv_string = file.read()
                dictionaries = cls.from_csv_string(csv_string)
                instances = [cls.create(**dic) for dic in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        for rect in list_rectangles:
            print("Rectangle: x={}, y={}, width={}, height={}".format(rect.x, rect.y, rect.width, rect.height))

        for square in list_squares:
            print("Square: x={}, y={}, size={}".format(square.x, square.y, square.size))
