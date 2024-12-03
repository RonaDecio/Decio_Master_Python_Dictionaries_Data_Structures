# Creating a dictionary of 8 planets and their distances from the Sun (in million kilometers)
planet_distances_dict = {
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.3,
    'Saturn': 1427.0,
    'Uranus': 2871.0,
    'Neptune': 4497.1
}

# Print the entire dictionary
print("The entire dictionary:", planet_distances_dict)

# Access and print the distance of the 3rd planet (Earth)
third_planet_distance = list(planet_distances_dict.values())[2]  # Index 2 for the 3rd planet
print("\nThe distance of the 3rd planet (Earth):", third_planet_distance, "million kilometers")

# Update the distance of the 5th planet (Jupiter)
planet_distances_dict['Jupiter'] = 800.0  # Updating the distance of Jupiter
print("\nUpdated distance of the 5th planet (Jupiter):", planet_distances_dict['Jupiter'], "million kilometers")

# Delete the 7th planet (Uranus) from the dictionary
del planet_distances_dict['Uranus']
print("\nDictionary after deleting the 7th planet (Uranus):", planet_distances_dict)

# Print the last key-value pair in the dictionary
last_key = list(planet_distances_dict.keys())[-1]
last_value = planet_distances_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
