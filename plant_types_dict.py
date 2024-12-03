# Creating a dictionary of 8 plants and their types
plant_types_dict = {
    'Rose': 'Shrub',
    'Oak': 'Tree',
    'Basil': 'Herb',
    'Cactus': 'Succulent',
    'Tulip': 'Flowering Plant',
    'Fern': 'Fern',
    'Lavender': 'Herb',
    'Pine': 'Tree'
}

# Print the entire dictionary
print("The entire dictionary:", plant_types_dict)

# Access and print the type of the 5th plant (Tulip)
fifth_plant_type = list(plant_types_dict.values())[4]  # Index 4 for the 5th plant
print("\nThe type of the 5th plant (Tulip):", fifth_plant_type)

# Update the type of the 2nd plant (Oak)
plant_types_dict['Oak'] = 'Deciduous Tree'  # Updating the type
print("\nUpdated type of the 2nd plant (Oak):", plant_types_dict['Oak'])

# Delete the 6th plant (Fern) from the dictionary
del plant_types_dict['Fern']
print("\nDictionary after deleting the 6th plant (Fern):", plant_types_dict)

# Print the last key-value pair in the dictionary
last_key = list(plant_types_dict.keys())[-1]
last_value = plant_types_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
