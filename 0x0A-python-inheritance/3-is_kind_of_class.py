#!/usr/bin/python3
""" Inhirtence modual """


def is_kind_of_class(obj, a_class):
    """ Check if an object is an instance of a class

    Args:
      obj (object): Object to check.
      a_class: Class to check.

    Return:
      True if the object is instance of the class False otherwise
    """
    return (isinstance(obj, a_class))
