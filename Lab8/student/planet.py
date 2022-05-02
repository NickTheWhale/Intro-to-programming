"""
Name:       DO_01: <Fill in your name>
Course:     CS1430, Section DO_02 :<Insert section here>,  Spring 2022
Assignment: Lab 08
Purpose:    This program implements a solar system. It uses the classes
            solarsystem.py, sun.py, planet.py
Input:      A sun, it's planets, and moons
Output:     Information about the planets in the solar system, and a
            table of volume and surface area of a sun with varying radii.
"""
#########################
# IMPORTS
#########################
import math

#########################
# CONSTANTS
#########################


class Planet:
    """
    The planet object represents a planet in the solar system.
    author(s): Donna Gavin
    """
    def __init__(self, i_name, i_radius, i_mass, i_dist, i_moons):
        """
        Default Constructor
        :param i_name: Name of the planet
        :type i_name: String
        :param i_radius: radius of the planet
        :type i_radius: int
        :param i_mass: mass of the planet
        :type i_mass: int
        :param i_dist: planet distance from the sun
        :type i_dist: int
        :param i_moons: number of moons
        :type i_moons: int
        """
        self.__name = i_name
        self.__radius = i_radius
        self.__mass = i_mass
        self.__distance = i_dist
        self.__moons = i_moons
        self.__moon_list = []

        # DO_03: Add the following attributes (variables) for the Planet class,
        #        assigning them to the parameters in the parameter list.
        #        The name attribute has already been created for you.
        #        Use the prefix self.__ before each attribute name.
        # b.	radius
        # c.	mass
        # d.	distance
        # e.	moons
        # f.	moon_list (initialize it to an empty list)

    @property
    def name(self):
        """
        Getter (accessor) for the planet name
        :return: the planet name
        :rtype: String
        """
        return self.__name
    
    @name.setter
    def name(self, new_name):
        """
        Setter (mutator) for the planet name
        :param new_name: New planet name
        :return: None
        """
        self.__name = new_name

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, x):
        self.__radius = x

    @property
    def mass(self):
        return self.__radius

    @mass.setter
    def mass(self, x):
        self.__mass = x

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, x):
        self.__distance = x

    @property
    def moons(self):
        return self.__moons

    @moons.setter
    def moons(self, x):
        self.__moons = x

    @property
    def moon_list(self):
        return self.__moon_list

    # DO_04: Create the Accessor (getter) and mutator (setter) methods for each
    #        of the following attributes. The getter and setter methods for the
    #        attribute name has already been created for you above. Include
    #        the docstring for each method.
    # b.	radius
    # c.	mass
    # d.	distance
    # e.	moons
    # f.	moon_list
    #  For the getter methods, type @property before the function header of the
    #  getter method. For the setter methods, type @attribute.setter before the
    #  function header of the setter method. See the example above for the
    #  attribute name.


    # DO_04: Create the following methods for the Planet class.
    # 2.	add_moon method to append the name of a new_moon to the end of
    #       moon_list.
    # 3.	get_volume method to calculate the volume of a sphere (volume of
    #       object it’s called with, 4/3 times PI times radius cubed)
    # 4.	get_surface_area method to calculate the surface area of a sphere
    #       (4 times PI times radius squared)
    # 5.	get_density method to calculate the density of a sphere, using the
    #       mass divided by the volume
    # 6.	get_circumference method to calculate the circumference of a sphere
    #       (2 times PI times radius)

    def add_moon(self, new_moon):
        self.__moon_list.append(new_moon)

    def get_volume(self):
        return (4/3) * math.pi * (self.__radius * self.__radius)

    def get_surface_area(self):
        return 4 * math.pi * (self.__radius * self.__radius)

    def get_density(self):
        return self.__mass / self.get_volume()

    def get_circumference(self):
        return 2 * math.pi * self.__radius
