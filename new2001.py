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

# n = 1092
#

# def digital_root(number):
#     while True:
#         sum = 0
#         while number > 0:
#             digit = number % 10
#             number = int(number / 10)
#             sum += digit
#         number = sum
#         if sum < 10:
#             break
#     return sum
#
#
# print(digital_root(n))
x = [1, 2, 2, 2, 3]
y = [2, 1]

# s = dict.fromkeys(x)
# print(list(s))
# result = x-y
# print(result)

# def array_diff(a: list, b: list):
#     for sub_b in b:
#         for sub_a in a:
#             if sub_a != sub_b:
#                 a.remove(sub_a)


# def array_diff(a: list, b: list):
#     return [item for item in a if item not in b]
#
#
# print(array_diff(x, y))
x = [2, 4, 0, 100, 4, 11, 2602, 36]
y = [160, 3, 1719, 19, 11, 13, -21]
#
#
#
# def find_outlier(integers: list):
#     for number in integers:
#         if integers[0] % 2 == 0 and integers[1] % 2 == 0:
#             if number % 2 != 0:
#                 return number
#         if integers[0] % 2 != 0 and integers[1] % 2 != 0:
#             if number % 2 == 0:
#                 return number
#
#
# print(find_outlier(x))
# print(find_outlier(y))


# def find_outlier(integers: list):
#     counter_odd = 0
#     counter_even = 0
#     for number in integers:
#         if number % 2 != 0:
#             counter_odd += 1
#
#         if number % 2 == 0:
#             counter_even += 1
#
#         # if counter_odd == 1:
#         #     return number % 2 != 0
#         #
#         # if counter_even == 1:
#         #     return number % 2 == 0
#
# find_outlier(x)


# def find_outlier(integers: list):
#     remainder = 1
#
#     if (integers[0] + integers[1]) % 2 == 0:
#         if integers[0] % 2 != 0:
#             remainder = 0
#     else:
#         if (integers[0] + integers[1] + integers[2]) % 2 == 0:
#             remainder = 0
#
#     for number in integers:
#         if number % 2 == remainder:
#             return number
#
#
# print(find_outlier(x))
# print(find_outlier(y))


x = 230


# def withdraw(n: int):
#     result = []
#     if n % 100 == 0:
#         return [n/100, 0, 0]
#
#     if n % 20 == 0:
#         result.append(n//100)
#         n = n % 100
#         result.append(0)
#         result.append(n//20)
#         return result
#
#     reminder = n % 50
#     if reminder % 20 == 0:
#         result.append(n // 100)
#         n = n % 100
#         result.append(1)
#         n = n - 50
#         result.append(n // 20)
#         return result
#     else:
#         result.append((n // 100) - 1)
#         n = (n % 100) + 100
#         result.append(1)
#         n = n - 50
#         result.append(n // 20)
#         return result



# x = 230
#
#
# def withdraw(n):
#     n50 = 0
#     n20, r = divmod(n, 20)
#     if r == 10:
#         n20 -= 2
#         n50 += 1
#     n100, n20 = divmod(n20, 5)
#     return [n100, n50, n20]
#
#
# print(withdraw(x))

x = "(()))((()())())"


def valid_parentheses(text: str):
    counter = 0
    if len(text) == 0:
        return True

    for character in text:
        if ord(character) == 40:
            counter += 1
        elif ord(character) == 41:
            counter -= 1

        if counter < 0:
            return False

    return counter == 0


print(valid_parentheses(x))