# x = [[23, 36, 48, 56, 28],
#      [87, 94, 17, 11, 74],
#      [82, 28, 41, 39, 43],
#      [97, 73, 68, 61, 65],
#      [55, 44, 33, 22, 51]]


# def snail(snail_map: list):
#     result = []
#     while snail_map:
#         for element in snail_map[0]:
#             result.append(element)
#         snail_map.remove(snail_map[0])
#
#         if not snail_map:
#             break
#
#         snail_map[0].reverse()
#
#         for element in snail_map[0]:
#             result.append(element)
#         snail_map.remove(snail_map[0])
#
#     return result
#
#
# print(snail(x))


# def snail(snail_map: list):
#     result = []
#     while snail_map:
#         for element in snail_map[0]:
#             result.append(element)
#         snail_map.remove(snail_map[0])
#
#         if not snail_map:
#             break
#
#         for _ in range(len(snail_map[0])):
#             result.append(snail_map[0].pop())
#         snail_map.remove(snail_map[0])
#
#     return result
#
#
# print(snail(x))

# sample = [[1,  2, 3],
#           [8, 9, 4],
#           [7, 6, 5]]
#
#
# def snail(snail_map: list):
#     result = []
#     while snail_map:
#
#         for element in snail_map[0]:
#             result.append(element)
#         snail_map.remove(snail_map[0])
#
#         if not snail_map:
#             break
#
#         for element in snail_map:
#             result.append(element.pop())
#
#         if not snail_map:
#             break
#
#         snail_map[-1].reverse()
#
#         for element in snail_map[-1]:
#             result.append(element)
#         snail_map.remove(snail_map[-1])
#
#         if not snail_map:
#             break
#
#         snail_map.reverse()
#
#         for element in snail_map:
#             element.reverse()
#             result.append(element.pop())
#             element.reverse()
#
#         snail_map.reverse()
#
#     return result
#
#
# print(snail(x))

c = ["gray","black","purple","purple","gray","black","gray","gray", "gray"]
from collections import Counter

new_dict = Counter(c)
print(new_dict)
x = int(5.7)
print(x)
