class SolarSystem:
    """
    This class represents a sun and it's planets
    Author(s): Donna Gavin
    """
    def __init__(self, a_sun):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        self.__the_sun = a_sun
        self.__planets = []

    @property
    def the_sun(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.__the_sun

    @property
    def planets(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.__planets

    def get_planet(self, planet_index):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return self.__planets[planet_index]

    def add_planet(self, a_planet):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        self.__planets.append(a_planet)

    def show_planets(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        for a_planet in self.planets:
            print(f"{a_planet} Moons: ",  end="")
            for i in range(a_planet.num_moons):
                if i == a_planet.num_moons - 1:
                    print(f"{a_planet.moon_list[i]}")
                else:
                    print(f"{a_planet.moon_list[i]}, ", end="")

    def num_planets(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        return len(self.planets)

    def get_total_mass(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        total_mass = self.the_sun.mass
        for a_planet in self.__planets:
            total_mass += a_planet.mass
        return total_mass

    def remove_planet(self, planet_name):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        for a_planet in self.__planets:
            if planet_name == a_planet.name:
                self.__planets.remove(a_planet)

    def get_nearest(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        d_min = self.planets[0].distance
        for i in range(1, len(self.planets)):
            if self.planets[i].distance < d_min:
                d_min = self.planets[i].distance
        return d_min

    def get_farthest(self):
        """
        :return: radius
        :rtype:
        :param:
        :type:
        """
        d_max = self.planets[0].distance
        for i in range(1, len(self.planets)):
            if self.planets[i].distance > d_max:
                d_max = self.planets[i].distance
        return d_max
