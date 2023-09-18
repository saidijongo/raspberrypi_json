import json

# Read JSON data from an external file
with open('recipes2.json') as file:
    cocktails = json.load(file)

# Initialize variables to keep track of total motors
total_motors = 0

# Iterate through cocktails and count motors
for cocktail_name, cocktail_data in cocktails.items():
    ingredients = cocktail_data.get("ingredients", [])
    print(f'Cocktail: {cocktail_name}')
    for ingredient in ingredients:
        name = ingredient.get("name", "")
        motor = ingredient.get("motor", 0)
        total_motors += motor
        print(f'  {name}: Motor {motor}')

# Print the total number of motors
print(f'Total number of motors: {total_motors}')
