# Creating a dictionary of 10 music albums and their release years (2018 to 2024)
music_albums_dict = {
    'Future Nostalgia': 2020,
    'Lover': 2019,
    'After Hours': 2020,
    'Folklore': 2020,
    'Scorpion': 2018,
    'Fine Line': 2019,
    'What’s Your Pleasure?': 2020,
    'Chromatica': 2020,
    'Positions': 2020,
    'Fearless (Taylor’s Version)': 2021
}

# Print the entire dictionary
print("The entire dictionary:", music_albums_dict)

# Access and print the release year of the 3rd album (After Hours)
third_album_year = list(music_albums_dict.values())[2]  # Index 2 for the 3rd album
print("\nThe release year of the 3rd album (After Hours):", third_album_year)

# Update the release year of the 8th album (Chromatica)
music_albums_dict['Chromatica'] = 2021  # Updating the release year
print("\nUpdated release year of the 8th album (Chromatica):", music_albums_dict['Chromatica'])

# Delete the 5th album (Scorpion) from the dictionary
del music_albums_dict['Scorpion']
print("\nDictionary after deleting the 5th album (Scorpion):", music_albums_dict)

# Print the last key-value pair in the dictionary
last_key = list(music_albums_dict.keys())[-1]
last_value = music_albums_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
