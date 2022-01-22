# numbers = [3, 5, 6, 7, 2, 6, 1, 3, 3, 9]
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]


# def create_phone_number(n):
#     num = ''.join(str(x) for x in n)
#     num1 = num[:3]
#     num2 = num[3:6]
#     num3 = num[6:]
#     # print(f"({num1}) {num2}-{num3}")
#     number = '(' + num1 + ')' + ' ' + num2 + '-' + num3
#     return number
#
#
# print(create_phone_number(numbers))
# print(create_phone_number(numbers1))

# x = 'AAAABBBCCDAABBB'
# y = ''


# def unique_in_order(iterable):
#     if len(iterable) < 1:
#         return []
#     result = []
#     element = iterable[0]
#     result.append(element)
#     for i in iterable[1:]:
#         if i != element:
#             result.append(i)
#         element = i
#     return result
#
#
# print(unique_in_order(x))
# print(unique_in_order(y))


# def unique_in_order(iterable):
#     result = []
#     element = None
#     for i in iterable[0:]:
#         if i != element:
#             result.append(i)
#             element = i
#     return result
#
#
# print(unique_in_order(x))
# print(unique_in_order(y))


# x = 'xxOOoo'


# def xo(s: str):
#     # str1 = s.upper()
#     # if str1.count('X') == str1.count('O'):
#     #     return True
#     # return False
#
# print(xo(x))

# x = ["Justyna", "Kuba"]
# y = ["Justyna"]
# z = ["Justyna", "Kuba", "Ola", "Jasiu", "Agnieszka"]
# a = []
# b = ['Justyna', 'Kuba', 'Ola']
# #
#
# def likes(names):
#     if len(names) == 0:
#         return 'no one likes this'
#     if len(names) == 1:
#         return f'{names[0]} likes this'
#     if len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     if len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
#
# print(likes(a))
# print(likes(y))
# print(likes(x))
# print(likes(b))
# print(likes(z))


# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)
#
#
# print(likes(a))
# print(likes(y))
# print(likes(x))
# print(likes(b))
# print(likes(z))