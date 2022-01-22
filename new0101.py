x = int(input("Podaj liczbę: "))

line_counter = 1
astrix_counter = 1

while line_counter <= x:
    while astrix_counter <= line_counter:
        print("*", end="")
        astrix_counter += 1
    astrix_counter = 1
    line_counter += 1
    print()
