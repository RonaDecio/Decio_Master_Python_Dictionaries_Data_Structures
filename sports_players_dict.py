# Creating a dictionary of 10 sports and their most famous players
sports_players_dict = {
    'Football': 'Lionel Messi',
    'Basketball': 'Michael Jordan',
    'Tennis': 'Roger Federer',
    'Cricket': 'Sachin Tendulkar',
    'Baseball': 'Babe Ruth',
    'Boxing': 'Muhammad Ali',
    'Golf': 'Tiger Woods',
    'Rugby': 'Jonah Lomu',
    'Hockey': 'Wayne Gretzky',
    'Athletics': 'Usain Bolt'
}

# Print the entire dictionary
print("The entire dictionary:", sports_players_dict)

# Access and print the player of the 4th sport (Cricket)
fourth_sport_player = list(sports_players_dict.values())[3]  # Index 3 for the 4th item
print("\nThe player of the 4th sport (Cricket):", fourth_sport_player)

# Update the player of the 6th sport (Boxing)
sports_players_dict['Boxing'] = 'Floyd Mayweather'
print("\nUpdated player of the 6th sport (Boxing):", sports_players_dict['Boxing'])

# Delete the 10th sport (Athletics) from the dictionary
del sports_players_dict['Athletics']
print("\nDictionary after deleting the 10th sport (Athletics):", sports_players_dict)

# Print the last key-value pair in the dictionary
last_key = list(sports_players_dict.keys())[-1]
last_value = sports_players_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
