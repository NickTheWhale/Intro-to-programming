class SolarSystem:
    """
    This class represents a sun and it's planets
    Author(s): Donna Gavin
    """
    def __init__(self, a_sun):
        """
        Default constructor for a solar system
        :param a_sun: sun object
        :type a_sun:
        """
        self.__the_sun = a_sun
        self.__planets = []

    @property
    def the_sun(self):
        """
        Getter (accessor), returns the name of the sun
        :return: sun object
        :rtype: string
        """
        return self.__the_sun

    @property
    def planets(self):
        """
        Getter (accessor),returns the list of planets in this solar system
        :return: the list of planets in this solar system
        :rtype: a list
        """
        return self.__planets

    def get_planet(self, planet_index):
        """
        Returns the planet object at index planet_index
        :param planet_index: the index of the planet
        :type
        :return: planet object
        :rtype
        """
        return self.__planets[planet_index]

    def add_planet(self, a_planet):
        """
        Adds a planet to the solar system
        :param a_planet: Planet object
        :type a_planet: object
        :return: None
        """
        self.__planets.append(a_planet)

    def show_planets(self):
        """
        Prints the name of all of the planets in this solar system
        :return: None
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
        Returns the number of planets in this solar system
        :return: length of planet list
        :rtype: int
        """
        return len(self.planets)

    def get_total_mass(self):
        """
        Returns the mass of all of the sun and planets in this solar system, not
        including moons
        :return: total mass
        :rtype: float
        """
        total_mass = self.the_sun.mass
        for a_planet in self.__planets:
            total_mass += a_planet.mass
        return total_mass

    def remove_planet(self, planet_name):
        """
        Removes a planet named planet_name from this solar system
        :param planet_name: planet name to remove
        :type planet_name: String
        :return: None
        """
        for a_planet in self.__planets:
            if planet_name == a_planet.name:
                self.__planets.remove(a_planet)

    def get_nearest(self):
        """
        Returns the
        :return:
        :rtype
        """
        d_min = self.planets[0].distance
        for i in range(1, len(self.planets)):
            if self.planets[i].distance < d_min:
                d_min = self.planets[i].distance
        return d_min

    def get_farthest(self):
        """
        Returns the farthest planet
        :return:
        :rtype:
        """
        d_max = self.planets[0].distance
        for i in range(1, len(self.planets)):
            if self.planets[i].distance > d_max:
                d_max = self.planets[i].distance
        return d_max
