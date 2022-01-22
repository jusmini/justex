# x = 30
#
#
# def count(n: int):
#     number = 1
#     for sub in range(1, n + 1):
#         number = number * sub
#         result = len(str(number))
#     return result
#
#
# print(count(x))


# x = 50000000
# import math
#
#
# def count(n: int):
#     if n <= 0:
#         return 0
#     if n <= 1:
#         return 1
#     digits = 0
#     for i in range(2, n +1):
#         digits += math.log10(i)
#
#     return math.floor(digits) + 1
#
#
# print(count(x))

# a1 = ["live", "arp", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
#
# def in_array(array1: list, array2: list):
#     result = []
#     for subelement in array1:
#         for element in array2:
#             if subelement in element:
#                 if subelement not in result:
#                     result.append(subelement)
#     return sorted(result)
#
#
# print(in_array(a1, a2))

from collections import Counter

# y = ['Just', 'Michał', 'Michu', 'Kubson', 'Kubson']
# numbers = [2, 5, 7, 9, 11]
#
# for name, number in zip(y, numbers):
#     print(name, number)

# x = [0, 0]
#
#
# def move_zeros(numbers: list):
#     for number in numbers:
#         if number == 0:
#             a = number
#             numbers.remove(number)
#             numbers.append(a)
#     return numbers
#
#
# print(move_zeros(x))


x = 1


def create_spiral(n):
    if not isinstance(n, int):
        return []
    result = []
    number = 1
    l_boundary = -1
    r_boundary = n
    for index in range(0, n):
        result.append([0]*n)

    i = j = 0

    while number <= n * n:
        for i in range(i, r_boundary):
            result[j][i] = number
            number += 1

        for j in range(j + 1, r_boundary):
            result[j][i] = number
            number += 1

        for i in range(i - 1, l_boundary, -1):
            result[j][i] = number
            number += 1

        for j in range(j - 1, l_boundary + 1, -1):
            result[j][i] = number
            number += 1

        l_boundary += 1
        r_boundary -= 1
        i += 1

    return result


print(create_spiral(x))