# x = 'world'
#
#
# def solution(st: str):
#     return st[::-1]
#
#
# print(solution(x))


# x = 15
#
#
# def solution(number: int):
#     counter = 0
#     i = 1
#     for i in range(1, number):
#         if i % 3 == 0 or i % 5 == 0:
#             counter += i
#     return counter
#
#
# print(solution(x))

# x = [10]
# from collections import Counter
#
#
# def find_it(seq: list):
#     solution = Counter(seq)
#     for key, value in solution.items():
#         if value % 2 != 0:
#             return key
#
#
# print(find_it(x))


# x = 942
#
#
# def digital_root(n: int):
#     result = []
#     for sub in str(n):
#         result.append(int(sub))
#     return sum(result)
#
#
# print(digital_root(x))

n = 1092


def digital_root(number):
    while True:
        sum = 0
        while number > 0:
            digit = number % 10
            number = int(number / 10)
            sum += digit
        number = sum
        if sum < 10:
            break
    return sum


print(digital_root(n))
