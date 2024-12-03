# Creating a dictionary of 12 countries and their corresponding capitals
country_capital_dict = {
    'United States': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'Mexico': 'Mexico City',
    'Brazil': 'Brasília',
    'United Kingdom': 'London',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'Australia': 'Canberra',
    'Japan': 'Tokyo',
    'India': 'New Delhi'
}

# Print the entire dictionary
print("The entire dictionary:", country_capital_dict)

# Access and print the capital of the 5th country (United Kingdom)
fifth_country_capital = list(country_capital_dict.values())[4]  # Index 4 for the 5th item
print("\nThe capital of the 5th country (United Kingdom):", fifth_country_capital)

# Update the capital of the 8th country (Italy)
country_capital_dict['Italy'] = 'Milan'
print("\nUpdated capital of the 8th country (Italy):", country_capital_dict['Italy'])

# Delete the 11th country (Japan) from the dictionary
del country_capital_dict['Japan']
print("\nDictionary after deleting the 11th country (Japan):", country_capital_dict)

# Print the last key-value pair in the dictionary
last_key = list(country_capital_dict.keys())[-1]
last_value = country_capital_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
