# Creating a dictionary of 5 space telescopes and their missions
space_telescope_missions_dict = {
    'Hubble Space Telescope': 'Hubble Deep Field',
    'James Webb Space Telescope': 'First Light',
    'Chandra X-ray Observatory': 'Deep Field Survey',
    'Spitzer Space Telescope': 'Exoplanet Exploration',
    'Kepler Space Telescope': 'Kepler Planet Search'
}

# Print the entire dictionary
print("The entire dictionary:", space_telescope_missions_dict)

# Access and print the mission of the 3rd telescope (Chandra X-ray Observatory)
third_telescope_mission = list(space_telescope_missions_dict.values())[2]  # Index 2 for the 3rd telescope
print("\nThe mission of the 3rd telescope (Chandra X-ray Observatory):", third_telescope_mission)

# Update the mission of the 1st telescope (Hubble Space Telescope)
space_telescope_missions_dict['Hubble Space Telescope'] = 'Hubble Ultra Deep Field'  # Updating the mission
print("\nUpdated mission of the 1st telescope (Hubble Space Telescope):", space_telescope_missions_dict['Hubble Space Telescope'])

# Delete the 4th telescope (Spitzer Space Telescope) from the dictionary
del space_telescope_missions_dict['Spitzer Space Telescope']
print("\nDictionary after deleting the 4th telescope (Spitzer Space Telescope):", space_telescope_missions_dict)

# Print the last key-value pair in the dictionary
last_key = list(space_telescope_missions_dict.keys())[-1]
last_value = space_telescope_missions_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
