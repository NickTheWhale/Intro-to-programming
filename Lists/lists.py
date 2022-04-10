lst = [1, 2, 3, 4]
lst.insert(3, [2, 3, 4])

total = 0
for i in range(len(lst)):
    if type(lst[i]) == int:
        total += 1
    elif type(lst[i]) == list:
        total += len(lst[i])

print(lst)
print("total", total)
print(lst)
lst = lst * 2
print(lst)

lst2 = [2 ** x for x in range(0, 20, 2)]
print(lst2)
print(sum(lst2))