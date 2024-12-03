# Create a dictionary of 8 beaches and the countries they are located in
beaches_countries_dict = {
    'Bondi Beach': 'Australia',
    'Waikiki Beach': 'USA',
    'Copacabana Beach': 'Brazil',
    'Maya Bay': 'Thailand',
    'Santorini Beach': 'Greece',
    'Maldives Beach': 'Maldives',
    'Navagio Beach': 'Greece',
    'Zlatni Rat': 'Croatia'
}

# Print the entire dictionary
print("The entire dictionary:", beaches_countries_dict)

# Access and print the country of the 3rd beach (Copacabana Beach)
third_beach_country = list(beaches_countries_dict.values())[2]  # Index 2 for the 3rd beach
print("\nCountry of the 3rd beach (Copacabana Beach):", third_beach_country)

# Update the country of the 6th beach (Maldives Beach)
beaches_countries_dict['Maldives Beach'] = 'Sri Lanka'
print("\nUpdated country of the 6th beach (Maldives Beach):", beaches_countries_dict['Maldives Beach'])

# Delete the 5th beach (Santorini Beach) from the dictionary
del beaches_countries_dict['Santorini Beach']
print("\nDictionary after deleting the 5th beach (Santorini Beach):", beaches_countries_dict)

# Print the last key-value pair in the dictionary
last_key = list(beaches_countries_dict.keys())[-1]
last_value = beaches_countries_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
