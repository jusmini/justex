number = int(input("Podaj wielokrotność znaków: "))

counter = 1

for i in range(1, number + 1):
    for x in range(0, counter):
        print("#", end="")
    counter += 1
    print()
