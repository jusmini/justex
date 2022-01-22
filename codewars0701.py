# floors = 6
#
#
# def tower_builder(n_floors):
#     for n in range(1, n_floors + 1):
#         return '*' * n
#
#
# print(tower_builder(floors))
# -----------------------
# x = [1, 1, 1, 2, 1, 1]
#
#
# def find_uniq(arr):
#     for n in arr:
#         result = arr.count(n)
#         return result
#
#
# print(find_uniq(x))
# ----------------------------
# y = 'aahahah'
# letters_list = list(y)
# print(letters_list)
# recap_list = []
#
# for char in letters_list:
#     result = letters_list.count(char)
#     recap_list.append(result)
#
# new_dict = dict.fromkeys(letters_list, recap_list)
# print(new_dict)
# -------------------------
# input_num = [(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)]
#
#
# def open_or_senior(data):
#     output = []
#     for a, b in data:
#         if a >= 55 and b > 7:
#             result = 'Senior'
#             output.append(result)
#             return output
#         else:
#             result = 'Open'
#             output.append(result)
#             return output
#
#
# print(open_or_senior(input_num))

# ---------------------------
# names = ["Ryan", "Kieran", "Mark"]
#
#
# def friend(x):
#     my_friend = []
#     for i in x:
#         if len(i) == 4:
#             my_friend.append(i)
#     return my_friend
#
#
# print(friend(names))
# # -----------------------------
#
#
# def friend1(x):
#     return [f for f in x if len(f) == 4]
#
#
# print(friend1(names))