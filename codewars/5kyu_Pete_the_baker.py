def cakes(recipe, available):
    num_cake = 0
    is_exhausted = False
    while True:
        for ingredient in recipe.keys():
            if available.get(ingredient):
                available[ingredient] -= recipe[ingredient]
                if available[ingredient] < 0:
                    is_exhausted = True
                    break
            else:
                is_exhausted = True
                break
        else:
            num_cake += 1

        if is_exhausted:
            break

    return num_cake


# best practice
def cakes(recipe, available):
    return min([available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe])
