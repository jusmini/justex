# x = 'racer'
# y = ['crazer', 'carer', 'racar', 'caers', 'racer']
#
#
# from collections import Counter
#
#
# def anagrams(word: str, words: list):
#     result = []
#     letters_word = dict(Counter(word))
#     for sub_word in words:
#         sub_word_sorted = ''.join(sorted(sub_word))
#         letters_sub_word = dict(Counter(sub_word_sorted))
#         if letters_word == letters_sub_word:
#             result.append(sub_word)
#     return result
#
#
# print(anagrams(x, y))


# x = {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
# y = {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}
#
#
# # def cakes(recipe: dict, available: dict):
# #     index = 0
# #     result = []
# #     if len(recipe) > len(available):
# #         return 0
# #
# #     shared_ingredients = {k: available[k] for k in available if k in recipe and available[k] >= recipe[k]}
# #
# #     if len(shared_ingredients) == len(recipe):
# #         recipe = dict(sorted(recipe.items()))
# #         shared_ingredients = dict(sorted(shared_ingredients.items()))
# #         recipe_values = list(recipe.values())
# #         shared_values = list(shared_ingredients.values())
# #
# #         for r in range(0, len(recipe_values)):
# #             difference = shared_values[index]//recipe_values[index]
# #             index += 1
# #             result.append(difference)
# #         return min(result)
# #
# #     else:
# #         return 0
# #
# #
# # print(cakes(x, y))
#
#
# print(x.get('apple', 0))

x = 5000
y = 3


def beeramid(bonus: int, price: int):
    level = 0
    beer_sum = 0
    sq_number = 1
    counter = 1
    if bonus > 0 and price > 0:
        beers = bonus // price
        while beer_sum + sq_number <= beers:
            level += 1
            beer_sum += sq_number
            counter += 1
            sq_number = counter ** 2

        return level
    else:
        return 0


print(beeramid(x, y))


