#!/usr/bin/python3
"""
Class that defines a student.
"""

class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only the attributes in that list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on the given dictionary.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
