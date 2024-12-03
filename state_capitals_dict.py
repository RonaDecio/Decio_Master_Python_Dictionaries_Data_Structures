# Creating a dictionary of 10 states and their capitals
state_capitals_dict = {
    'California': 'Sacramento',
    'Texas': 'Austin',
    'Florida': 'Tallahassee',
    'New York': 'Albany',
    'Illinois': 'Springfield',
    'Pennsylvania': 'Harrisburg',
    'Ohio': 'Columbus',
    'Georgia': 'Atlanta',
    'North Carolina': 'Raleigh',
    'Michigan': 'Lansing'
}

# Print the entire dictionary
print("The entire dictionary:", state_capitals_dict)

# Access and print the capital of the 4th state (New York)
fourth_state_capital = list(state_capitals_dict.values())[3]  # Index 3 for the 4th state
print("\nThe capital of the 4th state (New York):", fourth_state_capital)

# Update the capital of the 9th state (North Carolina)
state_capitals_dict['North Carolina'] = 'Charlotte'  # Updating the capital
print("\nUpdated capital of the 9th state (North Carolina):", state_capitals_dict['North Carolina'])

# Delete the 7th state (Ohio) from the dictionary
del state_capitals_dict['Ohio']
print("\nDictionary after deleting the 7th state (Ohio):", state_capitals_dict)

# Print the last key-value pair in the dictionary
last_key = list(state_capitals_dict.keys())[-1]
last_value = state_capitals_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
