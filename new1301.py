# from collections import Counter
#
# x = ["red", "green", "red", "blue", "blue", "red"]
# y = ["red", "red", "red", "red", "red", "red"]
# a = ["red","red"]
# b = ["red","green","blue"]
# c = ["gray","black","purple","purple","gray","black"]
# d = []
# e = ["red","green","blue","blue","red","green","red","red","red"]
#
#
# def number_of_pairs(gloves: list):
#     result = 0
#     colors = dict(Counter(gloves))
#     for key, value in colors.items():
#         result += int(value/2)
#
#     return result
#
#
# print(number_of_pairs(x))
# print(number_of_pairs(y))
# print(number_of_pairs(a))
# print(number_of_pairs(b))
# print(number_of_pairs(c))
# print(number_of_pairs(d))
# print(number_of_pairs(e))




# def number_of_pairs(gloves: list):
#     result = 0
#     d = dict(Counter(gloves))
#
#     for key, value in d.items():
#         result += int(value / 2)
#
#     return result
#
#
# print(f"Moje : {number_of_pairs(e)}")

# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
#
# def in_array(array1, array2):
#     result = []
#     while array1:
#         for element in array2:


# x = "The sunset sets at twelve o' clockz."
# y = ''
#
#
# def alphabet_position(text: str):
#     numbers = []
#     for letter in list(text.upper()):
#         position = ord(letter) - 64
#         if 1 <= position <= 26:
#             numbers.append(str(position))
#     return ' '.join(numbers) if numbers else ""
#
#
# print(alphabet_position(y))