"""
Name: Donna Gavin
Assignment: Quadratic

"""
import math

def positive_quadratic_root(a, b, c):
    '''
    Assume a is not 0, and the Discriminant is positive
    :param a: an integer representing a
    :a type: int
    :param b: an integer representing b
    :a type: int
    :param c: an integer representing c
    :c type: int
    :return: the positive quadratic root
    :return type: float
    '''
    root1 = 0
    disc_value = b * b - 4 * a * c
    if disc_value >= 0:
        discr = math.sqrt(disc_value)
        if a != 0:
            root1 = (-b + discr) / (2 * a)

    return root1


def quadratic_root(a, b, c):
    '''
    Assume a is not 0, and the Discriminant is positive
    :param a: an integer representing a
    :a type: int
    :param b: an integer representing b
    :a type: int
    :param c: an integer representing c
    :c type: int
    :return: the positive quadratic root
    :return type: float
    '''
    root1 = 0
    root2 = 0
    disc_value = b * b - 4 * a * c
    if disc_value >= 0:
        discr = math.sqrt(disc_value)
        if a != 0:
            root1 = (-b + discr) / (2 * a)
            root2 = (-b - discr) / (2 * a)

    return root1, root2

def main():
    """
    Quadratic equation solver
    :return:
    """
    a = 5
    b = 10
    c = 2
    root1, root2 = quadratic_root(a, b, c)
    print(root1, root2)


if __name__ == "__main__":
    main()