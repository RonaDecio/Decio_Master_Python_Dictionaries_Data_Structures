# Creating a dictionary of 8 authors and their famous books
author_books_dict = {
    'J.K. Rowling': 'Harry Potter and the Sorcerer\'s Stone',
    'George Orwell': '1984',
    'J.R.R. Tolkien': 'The Lord of the Rings',
    'Agatha Christie': 'Murder on the Orient Express',
    'F. Scott Fitzgerald': 'The Great Gatsby',
    'Harper Lee': 'To Kill a Mockingbird',
    'Jane Austen': 'Pride and Prejudice',
    'Mark Twain': 'Adventures of Huckleberry Finn'
}

# Print the entire dictionary
print("The entire dictionary:", author_books_dict)

# Access and print the book of the 5th author (F. Scott Fitzgerald)
fifth_author_book = list(author_books_dict.values())[4]  # Index 4 for the 5th author
print("\nThe book of the 5th author (F. Scott Fitzgerald):", fifth_author_book)

# Update the book of the 7th author (Jane Austen)
author_books_dict['Jane Austen'] = 'Sense and Sensibility'  # Updating the book
print("\nUpdated book of the 7th author (Jane Austen):", author_books_dict['Jane Austen'])

# Delete the 6th author (Harper Lee) from the dictionary
del author_books_dict['Harper Lee']
print("\nDictionary after deleting the 6th author (Harper Lee):", author_books_dict)

# Print the last key-value pair in the dictionary
last_key = list(author_books_dict.keys())[-1]
last_value = author_books_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
