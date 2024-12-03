# Creating a dictionary of 10 apps and their user ratings
app_store_ratings_dict = {
    'WhatsApp': 4.7,
    'Instagram': 4.6,
    'Facebook': 4.4,
    'Snapchat': 4.3,
    'Twitter': 4.2,
    'TikTok': 4.9,
    'YouTube': 4.8,
    'Spotify': 4.5,
    'Messenger': 4.3,
    'Reddit': 4.1
}

# Print the entire dictionary
print("The entire dictionary:", app_store_ratings_dict)

# Access and print the rating of the 6th app (TikTok)
sixth_app_rating = list(app_store_ratings_dict.values())[5]  # Index 5 for the 6th item
print("\nThe rating of the 6th app (TikTok):", sixth_app_rating)

# Update the rating of the 8th app (Spotify)
app_store_ratings_dict['Spotify'] = 4.7  # Updating the rating of Spotify
print("\nUpdated rating of the 8th app (Spotify):", app_store_ratings_dict['Spotify'])

# Delete the 9th app (Messenger) from the dictionary
del app_store_ratings_dict['Messenger']
print("\nDictionary after deleting the 9th app (Messenger):", app_store_ratings_dict)

# Print the last key-value pair in the dictionary
last_key = list(app_store_ratings_dict.keys())[-1]
last_value = app_store_ratings_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
