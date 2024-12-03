# Creating a dictionary of 10 movies and their directors
movie_directors_dict = {
    'Inception': 'Christopher Nolan',
    'The Dark Knight': 'Christopher Nolan',
    'Interstellar': 'Christopher Nolan',
    'The Matrix': 'Wachowskis',
    'Pulp Fiction': 'Quentin Tarantino',
    'The Shawshank Redemption': 'Frank Darabont',
    'The Godfather': 'Francis Ford Coppola',
    'Fight Club': 'David Fincher',
    'Forrest Gump': 'Robert Zemeckis',
    'The Lion King': 'Roger Allers, Rob Minkoff'
}

# Print the entire dictionary
print("The entire dictionary:", movie_directors_dict)

# Access and print the director of the 5th movie (Pulp Fiction)
fifth_movie_director = list(movie_directors_dict.values())[4]  # Index 4 for the 5th item
print("\nThe director of the 5th movie (Pulp Fiction):", fifth_movie_director)

# Update the director of the 9th movie (Forrest Gump)
movie_directors_dict['Forrest Gump'] = 'Updated Director'
print("\nUpdated director of the 9th movie (Forrest Gump):", movie_directors_dict['Forrest Gump'])

# Delete the 7th movie (The Godfather) from the dictionary
del movie_directors_dict['The Godfather']
print("\nDictionary after deleting the 7th movie (The Godfather):", movie_directors_dict)

# Print the last key-value pair in the dictionary
last_key = list(movie_directors_dict.keys())[-1]
last_value = movie_directors_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
