# counter = 0
# while counter != 3:
#     name = input(f"{counter}. Jak masz na imię? ")
#     print("Cześć", name)
#     counter += 1


# a = 6
# while a > 5:
#     a = int(input("Podaj liczbę większą od 5: "))
#     print("Podano liczbę a =", a)
# print("Twoja liczba nie była większa od 5")


# book = 50
# while book > 30:
#     book = book * 0.8
#     print("Po przecenie 20% aktualna cena to: ", round(book, 2), "zł")
#     print("---------------------------------")
# print("\nIdę do księgarni!")


# number = 10
# while number < 20:
#     number += 1
#     if number == 15:
#         break
#     print("Aktualny numer to: ", number)
#
# print("Jestem poza pętlą")


# number = 10
# while number < 20:
#     number += 1
#     if number == 15:
#         continue
#     print("Aktualny numer to: ", number)
#
# print("Jestem poza pętlą")


# x = 2
# while x < 12:
#     print(sum(range(x)))
#     x += 1


# import random
#
# random_number = random.randint(0, 15)
# user_number = int(input("Dawaj numerek: "))
#
# while random_number != user_number:
#     if random_number > user_number:
#         print(f"Twoja podana liczba {user_number} jest za mała")
#     else:
#         print(f"Twoja podana liczba {user_number} jest za duża")
#     user_number = int(input("Dawaj numerek: "))
# print("Bang")

# ------------------------------------------------------
# x = int(input("Podaj liczbę całkowitą od 1 do 15: "))
#
# for i in range(0, x):
#     if x <= 15:
#         print(f"Silnia Twojej liczby to {}")
#     else:
#         print("Podałeś liczbę większą niż 15.")


# x = int(input("Podaj liczbę całkowitą od 1 do 5: "))
# result = 1
# counter = 1
#
# while counter <= x:
#     result = result * counter
#     counter += 1
# print(result)


# x = int(input("Podaj liczbę całkowitą od 1 do 5: "))
# result = 1
#
# for counter in range(1, x + 1):
#     result = result * counter
#
# print(result)

# -----------------------------------
import random
words = ['owoc', 'mysz', 'kot']
word = random.choice(words)

shuffled_list = list(word)
random.shuffle(shuffled_list)
print(shuffled_list)

# linie od 100 do 104 to jedno rozwiązanie
# x = input("Zgadnij słowo: ")

# while x != word:
#     x = input("Zgadnij słowo: ")
# print("Spróbuj jeszcze raz")

# linie od 107 d0 115 to rozwiązanie z pętlą nieskończoną
while True:
    x = input("Zgadnij słowo lub wciśnij q aby zakończyć: ")
    if x == "q" or x == "Q":
        print("Zakończono grę")
        break
    if x == word:
        print("Zgadza się!")
        break
    print("Spróbuj jeszcze raz")