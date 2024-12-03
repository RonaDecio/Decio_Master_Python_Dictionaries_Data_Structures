# Create a dictionary of 8 technologies and their innovators
technology_innovators_dict = {
    'Telephone': 'Alexander Graham Bell',
    'Light Bulb': 'Thomas Edison',
    'Airplane': 'Wright Brothers',
    'Computer': 'Charles Babbage',
    'Internet': 'Tim Berners-Lee',
    'Electric Motor': 'Nikola Tesla',
    'Laser': 'Theodore Maiman',
    'Smartphone': 'Steve Jobs'
}

# Print the entire dictionary
print("The entire dictionary:")
print(technology_innovators_dict)

# Access and print the innovator of the 4th technology (Computer)
fourth_technology_innovator = list(technology_innovators_dict.values())[3]  # Index 3 for the 4th technology
print("\nInnovator of the 4th technology (Computer):", fourth_technology_innovator)

# Update the innovator of the 2nd technology (Light Bulb)
technology_innovators_dict['Light Bulb'] = 'Joseph Swan'
print("\nUpdated innovator of the 2nd technology (Light Bulb):", technology_innovators_dict['Light Bulb'])

# Delete the 6th technology (Electric Motor) from the dictionary
del technology_innovators_dict['Electric Motor']
print("\nDictionary after deleting the 6th technology (Electric Motor):")
print(technology_innovators_dict)

# Print the last key-value pair in the dictionary
last_key = list(technology_innovators_dict.keys())[-1]
last_value = technology_innovators_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
