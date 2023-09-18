import json

# Read JSON data from an external file
with open('recipes2.json') as file:
    cocktails = json.load(file)

# Count the number of cocktails
num_cocktails = len(cocktails)
print(f'Total number of cocktails: {num_cocktails}')
