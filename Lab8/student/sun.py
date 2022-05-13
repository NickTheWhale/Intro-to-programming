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
        Getter (accessor) for the name of the sun
        :return: name
        :rtype: string
        :param:
        :type:
        """
        return self.__name

    @property
    def mass(self):
        """
        Getter (accessor) for the mass
        :return: mass
        :rtype: int
        :param:
        :type:
        """
        return self.__mass

    @property
    def radius(self):
        """
        Getter (accessor) for the radius
        :return: radius
        :rtype: int
        :param:
        :type:
        """
        return self.__radius

    @property
    def temperature(self):
        """
        Getter (accessor) for the temp
        :return: temp
        :rtype: int
        :param:
        :type:
        """
        return self.__temp

    @name.setter
    def name(self, new_name):
        """
        Setter (mutator) for the name of the sun
        :param new_name: new name
        :type
        :return: None
        :rtype:
        """
        self.__name = new_name

    @radius.setter
    def radius(self, new_radius):
        """
        Setter (mutator) for the radius of the sun
        :param new_radius:
        :type
        :return: radius
        :rtype: int
        """
        self.__radius = new_radius

    def get_volume(self):
        """
        returns the volume of the sun
        :return: volume
        :rtype: float
        :param:
        :type:
        """
        volume = 4 / 3 * math.pi * self.radius ** 3
        return volume

    def get_surface_area(self):
        """
        returns the surface area of the sun
        :return: surface area
        :rtype: float
        :param:
        :type:
        """
        surface_area = 4 * math.pi * self.radius ** 2
        return surface_area

    def get_density(self):
        """
        returns density of the sun
        :return: density
        :rtype: float
        :param:
        :type:
        """
        density = self.__mass / self.get_volume()
        return density

    def __str__(self):
        """
        returns the name of the sun
        :return: name of the sun
        :rtype: string
        :param:
        :type:
        """
        return self.name
