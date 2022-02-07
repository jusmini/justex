# from itertools import combinations
# distances = [50, 55, 56, 57, 58]
# max_dis = 163
# city = 3
#
#
# def choose_best_sum(t: int, k: int, ls: list):
#     result = -1
#     for element in set(combinations(ls, k)):
#         suma = sum(element)
#         if t >= suma > result:
#             result = suma
#     if result == -1:
#         return None
#     else:
#         return result
#
#
# print(choose_best_sum(max_dis, city, distances))

from collections import Counter

x = ["NORTH", "WEST", "SOUTH", "EAST"]


def dirReduc(arr: list):
    directions = dict(Counter(arr))
    north = directions.get('NORTH', 0)
    south = directions.get('SOUTH', 0)
    east = directions.get('EAST', 0)
    west = directions.get('WEST', 0)

    temp_1 = ['NORTH'] * (north - south) if north > south else ['SOUTH'] * (south - north)
    temp_2 = ['EAST'] * (east - west) if east > west else ['WEST'] * (west - east)

    return temp_1 + temp_2


print(dirReduc(x))
