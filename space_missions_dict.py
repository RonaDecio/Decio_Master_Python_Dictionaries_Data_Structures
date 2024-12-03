# Creating a dictionary of 5 space missions and their corresponding years
space_missions_dict = {
    'Apollo 11': 1969,
    'Mars Rover': 2021,
    'Voyager 1': 1977,
    'Hubble Space Telescope': 1990,
    'International Space Station': 1998
}

# Print the entire dictionary
print("The entire dictionary:", space_missions_dict)

# Access and print the year of the 3rd mission (Voyager 1)
third_mission_year = list(space_missions_dict.values())[2]  # Index 2 for the 3rd item
print("\nThe year of the 3rd mission (Voyager 1):", third_mission_year)

# Update the year of the 2nd mission (Mars Rover)
space_missions_dict['Mars Rover'] = 2020  # Updating the year of the Mars Rover mission
print("\nUpdated year of the 2nd mission (Mars Rover):", space_missions_dict['Mars Rover'])

# Delete the 4th mission (Hubble Space Telescope) from the dictionary
del space_missions_dict['Hubble Space Telescope']
print("\nDictionary after deleting the 4th mission (Hubble Space Telescope):", space_missions_dict)

# Print the last key-value pair in the dictionary
last_key = list(space_missions_dict.keys())[-1]
last_value = space_missions_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
