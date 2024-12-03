# Creating a dictionary of 8 historical events and their years
historical_events_dict = {
    'The Declaration of Independence': 1776,
    'The French Revolution': 1789,
    'World War I Begins': 1914,
    'World War II Begins': 1939,
    'The Moon Landing': 1969,
    'Fall of the Berlin Wall': 1989,
    'The September 11 Attacks': 2001,
    'The End of Apartheid in South Africa': 1994
}

# Print the entire dictionary
print("The entire dictionary:", historical_events_dict)

# Access and print the year of the 2nd event (The French Revolution)
second_event_year = list(historical_events_dict.values())[1]  # Index 1 for the 2nd event
print("\nThe year of the 2nd event (The French Revolution):", second_event_year)

# Update the year of the 7th event (The September 11 Attacks)
historical_events_dict['The September 11 Attacks'] = 2002  # Updating the year
print("\nUpdated year of the 7th event (The September 11 Attacks):", historical_events_dict['The September 11 Attacks'])

# Delete the 5th event (The Moon Landing) from the dictionary
del historical_events_dict['The Moon Landing']
print("\nDictionary after deleting the 5th event (The Moon Landing):", historical_events_dict)

# Print the last key-value pair in the dictionary
last_key = list(historical_events_dict.keys())[-1]
last_value = historical_events_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
