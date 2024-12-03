# Creating a dictionary of 8 athletes and their greatest achievements
athlete_achievements_dict = {
    'Usain Bolt': 'World record in 100m and 200m sprints',
    'Michael Phelps': 'Winning 23 Olympic gold medals',
    'Serena Williams': '23 Grand Slam singles titles',
    'Cristiano Ronaldo': '5 Ballon d\'Or awards',
    'Simone Biles': '4 Olympic gold medals in gymnastics',
    'LeBron James': '4 NBA championships',
    'Roger Federer': '20 Grand Slam singles titles',
    'Tom Brady': '7 Super Bowl championships'
}

# Print the entire dictionary
print("The entire dictionary:", athlete_achievements_dict)

# Access and print the achievement of the 5th athlete (Simone Biles)
fifth_athlete_achievement = list(athlete_achievements_dict.values())[4]  # Index 4 for the 5th athlete
print("\nThe achievement of the 5th athlete (Simone Biles):", fifth_athlete_achievement)

# Update the achievement of the 3rd athlete (Serena Williams)
athlete_achievements_dict['Serena Williams'] = 'Most Grand Slam singles titles in the Open Era (23 titles)'  # Updating the achievement
print("\nUpdated achievement of the 3rd athlete (Serena Williams):", athlete_achievements_dict['Serena Williams'])

# Delete the 7th athlete (Roger Federer) from the dictionary
del athlete_achievements_dict['Roger Federer']
print("\nDictionary after deleting the 7th athlete (Roger Federer):", athlete_achievements_dict)

# Print the last key-value pair in the dictionary
last_key = list(athlete_achievements_dict.keys())[-1]
last_value = athlete_achievements_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
