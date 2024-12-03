# Create a dictionary of 8 festivals and their locations
festival_locations_dict = {
    'Diwali': 'India',
    'Carnival': 'Brazil',
    'Oktoberfest': 'Germany',
    'Mardi Gras': 'USA',
    'Songkran': 'Thailand',
    'La Tomatina': 'Spain',
    'Holi': 'India',
    'Glastonbury': 'UK'
}

# Print the entire dictionary
print("The entire dictionary:")
print(festival_locations_dict)

# Access and print the location of the 4th festival (Mardi Gras)
fourth_festival_location = list(festival_locations_dict.values())[3]  # Index 3 for the 4th festival
print("\nLocation of the 4th festival (Mardi Gras):", fourth_festival_location)

# Update the location of the 6th festival (La Tomatina)
festival_locations_dict['La Tomatina'] = 'Spain (updated)'
print("\nUpdated location of the 6th festival (La Tomatina):", festival_locations_dict['La Tomatina'])

# Delete the 2nd festival (Carnival) from the dictionary
del festival_locations_dict['Carnival']
print("\nDictionary after deleting the 2nd festival (Carnival):")
print(festival_locations_dict)

# Print the last key-value pair in the dictionary
last_key = list(festival_locations_dict.keys())[-1]
last_value = festival_locations_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
