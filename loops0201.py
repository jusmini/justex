# x = 5
#
# for i in range(x, 0, -1):
#     print(" " * (x-i), end="")
#     print("*" * i)


# while True:
#     answer = input("Czy chcesz zakończyć działanie programu? ")
#     if answer.lower() == "tak":
#         break


# number = int(input("Podaj liczbę: "))
# x = 0
# result = 1
#
# while result < number:
#     x += 1
#     result = 3 ** x
#
# print(x)


x = 723

b_200 = int(x / 200)
x -= (b_200 * 200)
b_100 = int(x / 100)
x -= (b_100 * 100)
b_50 = int(x / 50)
x -= (b_50 * 50)
b_20 = int(x / 20)
x -= (b_20 * 20)
b_10 = int(x / 10)
x -= (b_10 * 10)
m_5 = int(x / 5)
x -= (m_5 * 5)
m_2 = int(x / 2)
x -= (m_2 * 2)
m_1 = int(x / 1)
x -= (m_1 * 1)

output = ""

if b_200:
    output += f""
print(f"Liczba banknotów dwustuzłotowych: {b_200}, Liczba banknotów stuzłotowych: {b_100}")
