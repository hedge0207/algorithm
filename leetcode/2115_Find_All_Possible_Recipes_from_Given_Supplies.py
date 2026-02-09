from collections import defaultdict


class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        recipe_per_omitted_supplies = defaultdict(list)
        omitted_supplies_per_recipe = defaultdict(set)
        supplies = set(supplies)

        def cook(recipe):
            uncooked_recipes = recipe_per_omitted_supplies.pop(recipe, [])
            for uncooked_recipe in uncooked_recipes:
                omitted_supplies_per_recipe[uncooked_recipe].remove(recipe)
                if len(omitted_supplies_per_recipe[uncooked_recipe]) == 0:
                    supplies.add(uncooked_recipe)
                    cook(uncooked_recipe)

        for i in range(len(recipes)):
            recipe = recipes[i]
            is_satisfied = True
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    recipe_per_omitted_supplies[ingredient].append(recipe)
                    omitted_supplies_per_recipe[recipe].add(ingredient)
                    is_satisfied = False
            if is_satisfied:
                supplies.add(recipe)
                cook(recipe)

        ans = []
        for recipe in recipes:
            if len(omitted_supplies_per_recipe[recipe]) == 0:
                ans.append(recipe)
        return ans