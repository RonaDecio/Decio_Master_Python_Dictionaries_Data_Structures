# Creating a dictionary of 8 artists and their top songs
artist_songs_dict = {
    'Taylor Swift': 'Shake It Off',
    'Ed Sheeran': 'Shape of You',
    'Adele': 'Hello',
    'Drake': 'God\'s Plan',
    'Billie Eilish': 'Bad Guy',
    'The Weeknd': 'Blinding Lights',
    'Bruno Mars': 'Uptown Funk',
    'Post Malone': 'Circles'
}

# Print the entire dictionary
print("The entire dictionary:", artist_songs_dict)

# Access and print the top song of the 3rd artist (Adele)
third_artist_song = list(artist_songs_dict.values())[2]  # Index 2 for the 3rd artist
print("\nThe top song of the 3rd artist (Adele):", third_artist_song)

# Update the top song of the 6th artist (The Weeknd)
artist_songs_dict['The Weeknd'] = 'Save Your Tears'  # Updating the top song
print("\nUpdated top song of the 6th artist (The Weeknd):", artist_songs_dict['The Weeknd'])

# Delete the 7th artist (Bruno Mars) from the dictionary
del artist_songs_dict['Bruno Mars']
print("\nDictionary after deleting the 7th artist (Bruno Mars):", artist_songs_dict)

# Print the last key-value pair in the dictionary
last_key = list(artist_songs_dict.keys())[-1]
last_value = artist_songs_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
