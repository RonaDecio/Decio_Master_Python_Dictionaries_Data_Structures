# Creating a dictionary of 8 animals and their corresponding sounds
animal_sounds_dict = {
    'Dog': 'Bark',
    'Cat': 'Meow',
    'Cow': 'Moo',
    'Duck': 'Quack',
    'Sheep': 'Baa',
    'Horse': 'Neigh',
    'Pig': 'Oink',
    'Lion': 'Roar'
}

# Print the entire dictionary
print("The entire dictionary:", animal_sounds_dict)

# Access and print the sound of the 4th animal (Duck)
fourth_animal_sound = list(animal_sounds_dict.values())[3]  # Index 3 for the 4th item
print("\nThe sound of the 4th animal (Duck):", fourth_animal_sound)

# Update the sound of the 7th animal (Pig)
animal_sounds_dict['Pig'] = 'Grunt'
print("\nUpdated sound of the 7th animal (Pig):", animal_sounds_dict['Pig'])

# Delete the 5th animal (Sheep) from the dictionary
del animal_sounds_dict['Sheep']
print("\nDictionary after deleting the 5th animal (Sheep):", animal_sounds_dict)

# Print the last key-value pair in the dictionary
last_key = list(animal_sounds_dict.keys())[-1]
last_value = animal_sounds_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
