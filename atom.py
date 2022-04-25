class Atom:
    """An element from the periodic table."""

    def __init__(self, symbol, atomic, mass, isotope=12):
        """
        Parameterized Constructor
        Constructs an Atom with the given values.
        :param symbol:
        :param atomic:
        :param mass:
        :param isotope:
        """
        self.__symbol = symbol
        self.__atomic = atomic
        self.__mass = mass
        self.__isotope = isotope

    def neutrons(self):
        """Returns the number of neutrons the element has"""
        number = self.__isotope - self.__atomic
        print(f"{self.__symbol} has {number} neutrons")
        return number

    def grams_to_moles(self, grams):
        """Converts the mass of an element in grams to moles"""
        moles = grams / self.__mass
        print(f"{grams:.1f} g is {moles:.1f} moles of {self.__symbol}")
        return moles

    def get(self, param):
        param = param.upper()
        if param == "SYMBOL":
            return self.__symbol
        elif param == "ATOMIC":
            return self.__atomic
        elif param == "MASS":
            return self.__mass
        elif param == "ISOTOPE":
            return self.__isotope

    def get_symbol(self):
        return self.__symbol

    def get_atomic(self):
        return self.__atomic

    def get_mass(self):
        return self.__mass

    def get_isotope(self):
        return self.__isotope

    def set_isotope(self, isotope):
        self.__isotope = isotope


def main():
    oxygen = Atom('O', 8, 15.999, 16)
    carbon = Atom('C', 6, 12.001)
    print(oxygen.get_symbol())
    print(oxygen.get_atomic())
    print(oxygen.get_mass())
    print(oxygen.get_isotope())
    oxygen.set_isotope(100)
    print(oxygen.get_isotope())

def fun():
    y = Atom('O', 8, 15.999, 16)
    print(type(y))

if __name__ == "__main__":
    main()