#########################
# IMPORTS
#########################
import math


class Sun:
    """
    A class to represent the sun, with a name, radius, mass, and temperature
    author(s): Donna Gavin
    """
    def __init__(self, i_name, i_radius, i_mass, i_temp):
        """
        Default constructor
        :param i_name: Name of the Sun
        :type i_name: String
        :param i_radius: the radius
        :type i_radius: int
        :param i_mass: the mass of the sun
        :type i_mass: int
        :param i_temp: the temperature of the sun
        :type i_temp: int
        """
        self.__name = i_name
        self.__radius = i_radius
        self.__mass = i_mass
        self.__temp = i_temp

    @property
    def name(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.__name

    @property
    def mass(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.__mass

    @property
    def radius(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.__radius

    @property
    def temperature(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.__temp

    @name.setter
    def name(self, new_name):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        self.__name = new_name

    @radius.setter
    def radius(self, new_radius):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        self.__radius = new_radius

    def get_volume(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        volume = 4 / 3 * math.pi * self.radius ** 3
        return volume

    def get_surface_area(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        surface_area = 4 * math.pi * self.radius ** 2
        return surface_area

    def get_density(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        density = self.__mass / self.get_volume()
        return density

    def __str__(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.name



