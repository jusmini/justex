# x = "(( @"
#
#
# def duplicate_encode(word):
#     word = word.lower()
#     result = []
#     loop_check = False
#     for index in range(len(word)):
#         for letter in word[:index]:
#             if letter == word[index]:
#                 loop_check = True
#                 result.append(')')
#                 break
#         if not loop_check:
#             for letter in word[index + 1:]:
#                 if letter == word[index]:
#                     loop_check = True
#                     result.append(')')
#                     break
#         if not loop_check:
#             result.append('(')
#         loop_check = False
#     return ''.join([element for element in result])
# #
# #
# # print(duplicate_encode(x))
# names = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"


# def meeting(s: str):
#     s = s.upper()
#     splited_list = s.split(';')
#     result = []
#     for element in splited_list:
#         name, surname = element.split(':')
#         result.append(f'({surname}, {name})')
#     result.sort()
#     return ''.join([element for element in result])


# def meeting(s: str):
#     return "".join(sorted([f'({el[1]}, {el[0]})'if el else '' for el in [element.split(':') if element else '' for element in s.upper().split(";")]]))
#
#
# print(meeting(names))
# ----------------------------------
# x = "www.codewars.comabout"


# def remove_url_anchor(url: str):
#     splited_list = url.split('#')
#     return ''.join(splited_list[0])
#
#
# print(remove_url_anchor(x))
# ---------------------------------
# x = 'Pig latin is cool !'
#
#
# def pig_it(text: str):
#    result = ''
#    string_words = text.split(' ')
#    special_char = ['!', '?', '.', ',']
#    for word in string_words:
#        word = word[1:] + word[0]
#        if word not in special_char:
#           word = word + 'ay '
#        result += word
#    if result[-1] == ' ':
#       result = result[:-1]
#    return result
#
#
# print(pig_it(x))

# i = 1
# result = []
#
# while len(result) < 20:
#    if i % 2 == 0 and i % 3 == 0:
#       result.append(i)
#    i += 1
# print(result)
# print(len(result))

x = '9*A43<6^aFO 141499cK872:582r)\'"C<U>s3^=MjVm|)]H3153~mJ`R)09146881171590000038310'


def increment_string(strng: str):
    if len(strng) == 0:
        return '1'
    if strng[-1].isdigit():
        counter_index = -2
        while len(strng) > abs(counter_index) and strng[counter_index].isdigit():
            counter_index -= 1
        tail = strng[counter_index + 1:]
        counter_zeros = 0
        for digit in tail:
            if int(digit) == 0:
                counter_zeros += 1
            else:
                break
        if int(tail) == 0 and counter_zeros > 0:
            counter_zeros -= 1
        elif int(tail[-1]) == 9 and (int(tail[-2]) == 9 or int(tail[-2]) == 0):
            counter_zeros -= 1
        return f'{strng[:counter_index + 1]}{"0" * counter_zeros}{int(tail) + 1}'
    else:
        return f'{strng}1'


print(increment_string(x))



