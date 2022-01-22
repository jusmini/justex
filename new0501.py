# people_dict = {'name': 'Justyna', 'surname': 'Minias', 'age': 24, 'address': 'Zachodnia 14'}
# animal_dict = dict(animaltype='cat', petname='Ziemniak', petage=2, colour='black')

class Animal:
    animal_type: str
    petname: str
    pet_age: int
    colour: str

    def __init__(self, animal_type, petname, pet_age, colour):
        self.animal_type = animal_type
        self.petname = petname
        self.pet_age = pet_age
        self.colour = colour

    def __str__(self):
        # return f"animal_type = {self.animal_type} "\
        #        f"petname = {self.petname} "\
        #        f"pet age = {self.pet_age} "\
        #        f"colour = {self.colour}"
        return f'dzien dobry {self.petname}'


cat1 = Animal('cat', 'Ziemniok', 3, 'grey')
cat2 = Animal(colour='black', petname='Enter', pet_age=6, animal_type='cat')

print(cat1.__str__())
print(cat2)
# print(cat1.animal_type)
