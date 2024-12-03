# Create a dictionary of 7 sports events and their corresponding years
sports_events_dict = {
    'Olympic Games': 2020,
    'FIFA World Cup': 2022,
    'Super Bowl': 2021,
    'Tour de France': 2020,
    'Wimbledon': 2021,
    'NBA Finals': 2022,
    'UEFA Champions League Final': 2021
}

# Print the entire dictionary
print("The entire dictionary:", sports_events_dict)

# Access and print the year of the 3rd sports event (Super Bowl)
third_event_year = list(sports_events_dict.values())[2]  # Index 2 for the 3rd event
print("\nYear of the 3rd sports event (Super Bowl):", third_event_year)

# Update the year of the 6th sports event (NBA Finals)
sports_events_dict['NBA Finals'] = 2023
print("\nUpdated year of the 6th sports event (NBA Finals):", sports_events_dict['NBA Finals'])

# Delete the 5th sports event (Wimbledon) from the dictionary
del sports_events_dict['Wimbledon']
print("\nDictionary after deleting the 5th sports event (Wimbledon):", sports_events_dict)

# Print the last key-value pair in the dictionary
last_key = list(sports_events_dict.keys())[-1]
last_value = sports_events_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
