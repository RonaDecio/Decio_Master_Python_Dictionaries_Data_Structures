# Creating a dictionary of 8 video games and their platforms
video_game_platforms_dict = {
    'The Last of Us': 'PlayStation 3, PlayStation 4',
    'Minecraft': 'PC, Xbox, PlayStation, Switch',
    'Fortnite': 'PC, Xbox, PlayStation, Switch',
    'Call of Duty: Warzone': 'PC, Xbox, PlayStation',
    'Red Dead Redemption 2': 'PC, Xbox, PlayStation',
    'Cyberpunk 2077': 'PC, Xbox, PlayStation',
    'Super Mario Odyssey': 'Switch',
    'The Witcher 3: Wild Hunt': 'PC, Xbox, PlayStation, Switch'
}

# Print the entire dictionary
print("The entire dictionary:", video_game_platforms_dict)

# Access and print the platform of the 2nd video game (Minecraft)
second_game_platform = list(video_game_platforms_dict.values())[1]  # Index 1 for the 2nd item
print("\nThe platform of the 2nd video game (Minecraft):", second_game_platform)

# Update the platform of the 6th video game (Cyberpunk 2077)
video_game_platforms_dict['Cyberpunk 2077'] = 'PC, Xbox, PlayStation, Stadia'  # Updating the platform of Cyberpunk 2077
print("\nUpdated platform of the 6th video game (Cyberpunk 2077):", video_game_platforms_dict['Cyberpunk 2077'])

# Delete the 4th video game (Call of Duty: Warzone) from the dictionary
del video_game_platforms_dict['Call of Duty: Warzone']
print("\nDictionary after deleting the 4th video game (Call of Duty: Warzone):", video_game_platforms_dict)

# Print the last key-value pair in the dictionary
last_key = list(video_game_platforms_dict.keys())[-1]
last_value = video_game_platforms_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
