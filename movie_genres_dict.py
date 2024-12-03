# Creating a dictionary of 8 movie genres and their corresponding example movies
movie_genres_dict = {
    'Action': 'Mad Max: Fury Road',
    'Comedy': 'The Hangover',
    'Drama': 'The Shawshank Redemption',
    'Horror': 'A Nightmare on Elm Street',
    'Romance': 'The Notebook',
    'Sci-Fi': 'Inception',
    'Animation': 'Toy Story',
    'Thriller': 'Se7en'
}

# Print the entire dictionary
print("The entire dictionary:", movie_genres_dict)

# Access and print the example movie of the 3rd genre (Drama)
third_genre_movie = list(movie_genres_dict.values())[2]  # Index 2 for the 3rd item
print("\nThe example movie of the 3rd genre (Drama):", third_genre_movie)

# Update the example movie of the 5th genre (Romance)
movie_genres_dict['Romance'] = 'Pride and Prejudice'  # Updating the example movie of Romance genre
print("\nUpdated example movie of the 5th genre (Romance):", movie_genres_dict['Romance'])

# Delete the 7th genre (Animation) from the dictionary
del movie_genres_dict['Animation']
print("\nDictionary after deleting the 7th genre (Animation):", movie_genres_dict)

# Print the last key-value pair in the dictionary
last_key = list(movie_genres_dict.keys())[-1]
last_value = movie_genres_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
