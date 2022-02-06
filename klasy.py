class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name = {self.name}\nage = {self.age}'


cat1 = Cat('ju', 3)
cat2 = Cat('Pyza', 1)
print(cat2.name, cat2.age)
print(cat1)
print(cat2)