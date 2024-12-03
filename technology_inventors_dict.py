# Creating a dictionary of 6 technologies and their inventors
technology_inventors_dict = {
    'Telephone': 'Alexander Graham Bell',
    'Lightbulb': 'Thomas Edison',
    'Airplane': 'Wright Brothers',
    'Computer': 'Charles Babbage',
    'Internet': 'Tim Berners-Lee',
    'Printing Press': 'Johannes Gutenberg'
}

# Print the entire dictionary
print("The entire dictionary:", technology_inventors_dict)

# Access and print the inventor of the 4th technology (Computer)
fourth_technology_inventor = list(technology_inventors_dict.values())[3]  # Index 3 for the 4th item
print("\nThe inventor of the 4th technology (Computer):", fourth_technology_inventor)

# Update the inventor of the 2nd technology (Lightbulb)
technology_inventors_dict['Lightbulb'] = 'Humphry Davy'  # Updating the inventor of the Lightbulb
print("\nUpdated inventor of the 2nd technology (Lightbulb):", technology_inventors_dict['Lightbulb'])

# Delete the 6th technology (Printing Press) from the dictionary
del technology_inventors_dict['Printing Press']
print("\nDictionary after deleting the 6th technology (Printing Press):", technology_inventors_dict)

# Print the last key-value pair in the dictionary
last_key = list(technology_inventors_dict.keys())[-1]
last_value = technology_inventors_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
