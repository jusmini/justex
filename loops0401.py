# wypisz najwieksza liczbe niepodzielna przez 2,3,5,7 ale mniejsza niz 1000
# x = -1
# outer_counter = 0
# inner_counter = 0
#
# for i in range(1, 1000):
#     outer_counter += 1
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
#         x = i
#         inner_counter += 1
# print(x)
# print(outer_counter, inner_counter)
# print()
# --------------------------
# x = -1
# outer_counter = 0
# inner_counter = 0
#
# for i in range(1000, 0, -1):
#     outer_counter += 1
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
#         x = i
#         inner_counter += 1
#         break
# print(x)
# print(outer_counter, inner_counter)



# zadanko 1
# while True:
#     x = input("Jeśli chcesz zakończyć działanie programu podaj Q: ")
#     if x.lower() == "q":
#         print("Zakończono grę")
#         break
    # else:
    #     print("POWTARZAM - ")

# zadanko 2
x = int(input("Podaj liczbę: "))
result = 1
power = 0

while result < x:
    power += 1
    result = 3 ** power
print(power)


# zadanko random
# import random
#
# random_number = random.randint(0, 20)
#
# while True:
#     user_number = int(input("Podaj liczbę: "))
#     if random_number > user_number:
#         print("Za mało! Spróbuj jeszcze raz!")
#     elif random_number < user_number:
#         print("Za dużo! Spróbuj jeszcze raz!")
#     else:
#         print("Bingo!")
#         break
