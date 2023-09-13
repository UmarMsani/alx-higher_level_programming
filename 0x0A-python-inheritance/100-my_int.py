#!/usr/bin/python3
"""To define class MyInt that inherits from int."""


class MyInt(int):
    """Custom integer class that inverts == and != operators."""

    def __eq__(self, number):
        """Override == operator to compare the inequality."""
        return self.real != number

    def __ne__(self, number):
        """Override != operator to compare the equality."""
        return self.real == number
