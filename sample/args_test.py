def displayPerson(*mystery):
    for i in mystery:
        print(i)

def main():
    name = "Brian"
    age = 20
    temp = 95.6
    displayPerson(age, temp, name )

main()