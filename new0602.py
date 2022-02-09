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

# from collections import Counter
#
# x = ["NORTH", "WEST", "SOUTH", "EAST"]
#
#
# def dirReduc(arr: list):
#     directions = dict(Counter(arr))
#     north = directions.get('NORTH', 0)
#     south = directions.get('SOUTH', 0)
#     east = directions.get('EAST', 0)
#     west = directions.get('WEST', 0)
#
#     temp_1 = ['NORTH'] * (north - south) if north > south else ['SOUTH'] * (south - north)
#     temp_2 = ['EAST'] * (east - west) if east > west else ['WEST'] * (west - east)
#
#     return temp_1 + temp_2
#
#
# print(dirReduc(x))


# x = 120
#
#
# def make_readable(seconds: int):
#     if 359999 >= seconds > 0:
#         hours = seconds//3600
#         difference = seconds - (hours * 3600)
#         minutes = difference//60
#         seconds = difference - (minutes * 60)
#
#         if hours <= 9:
#             hours = '0' + str(hours)
#         if minutes <= 9:
#             minutes = '0' + str(minutes)
#         if seconds <= 9:
#             seconds = '0' + str(seconds)
#
#         return f'{hours}:{minutes}:{seconds}'
#     else:
#         return '00:00:00'
#
#
# print(make_readable(x))


# x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]]
y = 'clockwise'


def rotate(matrix: list, direction: str):
    frame = []
    for sub_list in range(0, len(matrix[0])):
        frame.append([0] * len(matrix))

    if direction == 'clockwise':
        destination_column = len(matrix)-1
        start_row = 0
        row_increment = 1
        column_increment = -1
    else:
        destination_column = 0
        start_row = len(matrix[0])-1
        row_increment = -1
        column_increment = 1

    for sub_list in matrix:
        row = start_row
        for element in sub_list:
            frame[row][destination_column] = element
            row += row_increment
        destination_column += column_increment

    return frame

print(rotate(x, y))
