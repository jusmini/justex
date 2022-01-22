# floors = 6
#
#
# def tower_builder(n_floors):
#     space_couter = n_floors - 1
#     astrix_couter = 1
#     new_list = []
#     for n in range(0, n_floors):
#         new_list.append(f"{' ' * space_couter}{'*' * astrix_couter}{' ' * space_couter}")
#         astrix_couter += 2
#         space_couter -= 1
#     return new_list


# x = [1, 1, 1, 2, 1, 1]
#
#
# def find_uniq(arr: list):
#     arr.sort()
#     if arr[0] == arr[1]:
#         return arr[-1]
#     return arr[0]
#
#
# print(find_uniq(x))


# def find_uniq(arr: list):
#     arr.sort()
#     return arr[-1] if arr[0] == arr[1] else arr[0]


# y = 'aaba'
#
#
# def count(string):
#     new_dict = {}
#     counter = 0
#     prev_element = None
#     letters_list = list(string)
#     letters_list.sort()
#     for letter in letters_list:
#         if letter == prev_element:
#             counter += 1
#         else:
#             if prev_element != None:
#                 new_dict[prev_element] = counter
#             counter = 1
#             prev_element = letter
#     if prev_element != None:
#         new_dict[prev_element] = counter
#     return new_dict
#
#
# print(count(y))
# for char in letters_list:
#     result = letters_list.count(char)
#     recap_list.append(result)
#
# new_dict = dict.fromkeys(letters_list, recap_list)
# print(new_dict)

# input1 = [(16, 23),(73,1),(56, 20),(1, -1)]
#
#
# def open_or_senior(data):
#     new_list = []
#     # for item in data:
#     #     if item[0] >= 55 and item[1] > 7:
#     #         new_list.append('Senior')
#     #     else:
#     #         new_list.append('Open')
#     # return new_list
#     return ['Senior' for item in data if item[0] >= 55 and item[1] > 7]
#
#
# print(open_or_senior(input1))
