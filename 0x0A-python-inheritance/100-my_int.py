#!/usr/bin/python3
"""Definition  class MyInt that inherits int"""


class MyInt(int):
    """Inherits int operators == and !=."""

    def __eq__(self, value):
        """Override == opertor with != behvior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior. """
        return self.real == value
