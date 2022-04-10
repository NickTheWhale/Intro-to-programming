def add(x, lst = []):
    if not(x in lst):
        lst.append(x)
    return lst


def main():
    list1 = add(1)
    print(list1)
    list2 = add(2)
    print(list2)
    list3 = add(3, [11, 12, 13, 14])
    print(list3)
    list4 = add(4)
    print(list4)
    list5 = add(6, [9, 8])
    print(list5)


if __name__ == "__main__":
    main()
