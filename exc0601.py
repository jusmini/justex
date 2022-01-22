# def multiply(a, b):
#     return a * b
#
#
# x = multiply(2, 4)
# print(x)


# def hello(name: str):
#     print("Siemanko", name)
#
#
# hello('Justyna')

numbers = [3, 5, 6, 7, 2, 6, 1, 3, 3, 9]
num = ''.join(str(x) for x in numbers)
print(num)

num1 = num[:3]
print(num1)
num2 = num[3:6]
num3 = num[6:]
print(num2)
print(num3)
