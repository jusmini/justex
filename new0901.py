# x = -5
# for a in range(1, 10):
#     if x == 0 or a/x == 0.2:
#         continue
#     print(a/x)
#     x += 1
import itertools


# def next_bigger(n: int):
#     digits = [number for number in str(n)]
#     result = {''.join(item) for item in itertools.permutations(str(n), len(digits))}
#     result = sorted(result)
#     min_number = -1
#     for number in result:
#         if int(number) > n:
#             min_number = int(number)
#             break
#     return min_number
#
#
# print(next_bigger(x))
# x = 1234567908
#
#
# def next_bigger(n: int):
#     digits = list(str(n))
#
#     for i in range(len(digits) - 1, 0, -1):
#         if digits[i] > digits[i - 1]:
#             left = digits[:i]
#             right = sorted(digits[i:])
#
#             for x in range(len(right)):
#                 if left[-1] < right[x]:
#                     temp_num = left[-1]
#                     left[-1] = right[x]
#                     right[x] = temp_num
#                     return int("".join(left + right))
#
#     return -1
#
#
# print(next_bigger(x))
