import json

# Read JSON data from an external file
with open('recipes2.json') as file:
    cocktails = json.load(file)

# Create a dictionary to store ingredient names and their motor numbers
ingredient_motor_dict = {}

# Iterate through cocktails and collect ingredient data
for cocktail_name, cocktail_data in cocktails.items():
    ingredients = cocktail_data.get("ingredients", [])
    for ingredient in ingredients:
        name = ingredient.get("name", "")
        motor = ingredient.get("motor", 0)
        ingredient_motor_dict[name] = motor

# Sort the ingredient dictionary by motor numbers in ascending order
sorted_ingredients = sorted(ingredient_motor_dict.items(), key=lambda x: x[1])

# Print the sorted ingredient list with motor numbers
for ingredient, motor in sorted_ingredients:
    print(f'{ingredient}: Motor {motor}')
