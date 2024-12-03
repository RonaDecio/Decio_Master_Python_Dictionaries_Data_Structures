# Creating a dictionary of 8 animals and their natural habitats
animal_habitats_dict = {
    'Lion': 'Savannah',
    'Penguin': 'Antarctica',
    'Kangaroo': 'Australian Outback',
    'Elephant': 'Grasslands',
    'Polar Bear': 'Arctic',
    'Tiger': 'Tropical Rainforest',
    'Panda': 'Bamboo Forests',
    'Whale': 'Ocean'
}

# Print the entire dictionary
print("The entire dictionary:", animal_habitats_dict)

# Access and print the habitat of the 3rd animal (Kangaroo)
third_animal_habitat = list(animal_habitats_dict.values())[2]  # Index 2 for the 3rd item
print("\nThe habitat of the 3rd animal (Kangaroo):", third_animal_habitat)

# Update the habitat of the 5th animal (Polar Bear)
animal_habitats_dict['Polar Bear'] = 'Frozen Tundra'
print("\nUpdated habitat of the 5th animal (Polar Bear):", animal_habitats_dict['Polar Bear'])

# Delete the 7th animal (Panda) from the dictionary
del animal_habitats_dict['Panda']
print("\nDictionary after deleting the 7th animal (Panda):", animal_habitats_dict)

# Print the last key-value pair in the dictionary
last_key = list(animal_habitats_dict.keys())[-1]
last_value = animal_habitats_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
