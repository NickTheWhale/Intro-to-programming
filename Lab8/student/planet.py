"""
Name:       DO_01: Nicholas Loehrke
Course:     CS1430, Section DO_02 :02,  Spring 2022
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
    def __init__(self, i_name, i_radius, i_mass, i_dist, i_num_moons):
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
        :param i_num_moons: number of moons
        :type i_num_moons: int
        """
        self.__name = i_name
        self.__radius = i_radius
        self.__mass = i_mass
        self.__distance = i_dist
        self.__num_moons = i_num_moons
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
        :param:
        :type:
        """
        return self.__name
    
    @name.setter
    def name(self, new_name):
        """
        Setter (mutator) for the planet name
        :param new_name: New planet name
        :return: None
        :rtype:
        :type:
        """
        self.__name = new_name

    @property
    def radius(self):
        """
        Getter (accessor) for the planet radius
        :return: the planet radius
        :rtype: Int
        :param:
        :type:
        """
        return self.__radius

    @radius.setter
    def radius(self, x):
        """
        Setter (mutator) for the planet radius
        :param radius: New planet name
        :return: None
        :rtype:
        :type:
        """
        self.__radius = x

    @property
    def mass(self):
        """
        Getter (accessor) for the planet mass
        :return: the planet mass
        :rtype: Int
        :param:
        :type:
        """
        return self.__mass

    @mass.setter
    def mass(self, x):
        """
        Setter (mutator) for the planet mass
        :param mass: New planet mass
        :return: None
        :rtype:
        :type:
        """
        self.__mass = x

    @property
    def distance(self):
        """
        Getter (accessor) for the planet distance from the sun
        :return: the planet distance from the sun
        :rtype: Int
        :param:
        :type:
        """
        return self.__distance

    @distance.setter
    def distance(self, x):
        """
        Setter (mutator) for the planet distance from the sun
        :param distance: New planet distance
        :return: None
        :rtype:
        :type:
        """
        self.__distance = x

    @property
    def num_moons(self):
        """
        Getter (accessor) for the planet number of moons
        :return: the planet number of moons
        :rtype: Int
        :param:
        :type:
        """
        return self.__num_moons

    @num_moons.setter
    def num_moons(self, x):
        """
        Setter (mutator) for the planet number of moons
        :param num_moons: New planet number of moons
        :return: None
        :rtype:
        :type:
        """
        self.__num_moons = x

    @property
    def moon_list(self):
        """
        Getter (accessor) for list of moons for each planet
        :return: the list of moons for each planet
        :rtype: List
        :param:
        :type:
        """
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
        """
        Adds a new moon to the list of moons
        :return: None
        :rtype:
        :param:
        :type:
        """
        self.__moon_list.append(new_moon)

    def get_volume(self):
        """
        Getter (accessor) for the planet volume
        :return: the planet volume
        :rtype: Int
        :param:
        :type:
        """
        return (4/3) * math.pi * (self.radius * self.radius * self.radius)

    def get_surface_area(self):
        """
        Getter (accessor) for the planet surface area
        :return: the planet surface area
        :rtype: Int
        :param:
        :type:
        """
        return 4 * math.pi * (self.radius * self.radius)

    def get_density(self):
        """
        Getter (accessor) for the planet density
        :return: the planet density
        :rtype: Int
        :param:
        :type:
        """
        return self.mass / self.get_volume()

    def get_circumference(self):
        """
        Getter (accessor) for the planet circumference
        :return: the planet circumference
        :rtype: Int
        :param:
        :type:
        """
        return 2 * math.pi * self.radius
