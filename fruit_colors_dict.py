# Creating a dictionary of 8 fruits and their corresponding colors
fruit_colors_dict = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Orange': 'Orange',
    'Grapes': 'Purple',
    'Blueberry': 'Blue',
    'Strawberry': 'Red',
    'Pineapple': 'Yellow',
    'Watermelon': 'Green'
}

# Print the entire dictionary
print("The entire dictionary:", fruit_colors_dict)

# Access and print the color of the 6th fruit (Strawberry)
sixth_fruit_color = list(fruit_colors_dict.values())[5]  # Index 5 for the 6th item
print("\nThe color of the 6th fruit (Strawberry):", sixth_fruit_color)

# Update the color of the 4th fruit (Grapes)
fruit_colors_dict['Grapes'] = 'Green'
print("\nUpdated color of the 4th fruit (Grapes):", fruit_colors_dict['Grapes'])

# Delete the 7th fruit (Pineapple) from the dictionary
del fruit_colors_dict['Pineapple']
print("\nDictionary after deleting the 7th fruit (Pineapple):", fruit_colors_dict)

# Print the last key-value pair in the dictionary
last_key = list(fruit_colors_dict.keys())[-1]
last_value = fruit_colors_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
