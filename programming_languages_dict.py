# Creating a dictionary of 7 programming languages and their developers
programming_languages_dict = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'C++': 'Bjarne Stroustrup',
    'JavaScript': 'Brendan Eich',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'Swift': 'Chris Lattner'
}

# Print the entire dictionary
print("The entire dictionary:", programming_languages_dict)

# Access and print the developer of the 4th programming language (JavaScript)
fourth_language_developer = list(programming_languages_dict.values())[3]  # Index 3 for the 4th item
print("\nThe developer of the 4th programming language (JavaScript):", fourth_language_developer)

# Update the developer of the 6th programming language (PHP)
programming_languages_dict['PHP'] = 'Andi Gutmans'
print("\nUpdated developer of the 6th programming language (PHP):", programming_languages_dict['PHP'])

# Delete the 2nd programming language (Java) from the dictionary
del programming_languages_dict['Java']
print("\nDictionary after deleting the 2nd programming language (Java):", programming_languages_dict)

# Print the last key-value pair in the dictionary
last_key = list(programming_languages_dict.keys())[-1]
last_value = programming_languages_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
