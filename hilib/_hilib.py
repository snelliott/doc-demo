""" _hilib module docstring
"""
import numpy


def greet_me(name='Jim'):
    """ Greet me by name

    :param name: my name
    :type name: str
    :returns: nothing
    :rtype: NoneType

    """
    print("Hi there {:s}.".format(name))


def announce_the_weather():
    """ Tell me the weather today

    :returns: nothing
    :rtype: NoneType

    """
    print(numpy.random.choice(["Sunny", "Rainy", "Cloud"]))
