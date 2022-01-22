# zadanie 6
# result = 0
#
# for i in range(1, 5):
#     result = result + i
# print(result)


# zadanie 7
# result = 0
# number = 5
#
# for i in range(1, 460):
#     result = result + number
#     number += 2
# print(result)


# zadanie 8
# x = 6
#
# for i in range(1, x + 1):
#     print("*" * i)


# zadanie 9
# x = 6
#
# for i in range(x, 0, -1):
#     print("*" * i)


# zadanie 10
# x = 6
#
# for i in range(x, 0, -1):
#     print(" " * (x-i), "*" * i)


# zadanie 6 ponownie
# result = 0
#
# for i in range(1, 460):
#     result += i
# print(result)


# zadnie 7 ponownie, wartość pierwszego wyrazu to 6 różnica to 3, liczymy do 199
result = 0
number = 6

for i in range(1, 199):
    result = result + number
    number += 3
print(result)
