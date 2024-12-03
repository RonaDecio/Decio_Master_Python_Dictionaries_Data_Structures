# Creating a dictionary of 6 rivers and their lengths in kilometers
river_lengths_dict = {
    'Nile': 6650,
    'Amazon': 6400,
    'Yangtze': 6300,
    'Mississippi': 3730,
    'Ganges': 2525,
    'Danube': 2850
}

# Print the entire dictionary
print("The entire dictionary:", river_lengths_dict)

# Access and print the length of the 2nd river (Amazon)
second_river_length = list(river_lengths_dict.values())[1]  # Index 1 for the 2nd item
print("\nThe length of the 2nd river (Amazon):", second_river_length)

# Update the length of the 5th river (Ganges)
river_lengths_dict['Ganges'] = 2600  # Updating the length of the Ganges river
print("\nUpdated length of the 5th river (Ganges):", river_lengths_dict['Ganges'])

# Delete the 4th river (Mississippi) from the dictionary
del river_lengths_dict['Mississippi']
print("\nDictionary after deleting the 4th river (Mississippi):", river_lengths_dict)

# Print the last key-value pair in the dictionary
last_key = list(river_lengths_dict.keys())[-1]
last_value = river_lengths_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
