# Creating a dictionary of 12 books and their authors
book_authors_dict = {
    '1984': 'George Orwell',
    'To Kill a Mockingbird': 'Harper Lee',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'Moby-Dick': 'Herman Melville',
    'Pride and Prejudice': 'Jane Austen',
    'War and Peace': 'Leo Tolstoy',
    'The Catcher in the Rye': 'J.D. Salinger',
    'The Hobbit': 'J.R.R. Tolkien',
    'The Lord of the Rings': 'J.R.R. Tolkien',
    'Crime and Punishment': 'Fyodor Dostoevsky',
    'Brave New World': 'Aldous Huxley',
    'Frankenstein': 'Mary Shelley'
}

# Print the entire dictionary
print("The entire dictionary:", book_authors_dict)

# Access and print the author of the 9th book (The Lord of the Rings)
ninth_book_author = list(book_authors_dict.values())[8]  # Index 8 for the 9th item
print("\nThe author of the 9th book (The Lord of the Rings):", ninth_book_author)

# Update the author of the 5th book (Pride and Prejudice)
book_authors_dict['Pride and Prejudice'] = 'Updated Author'
print("\nUpdated author of the 5th book (Pride and Prejudice):", book_authors_dict['Pride and Prejudice'])

# Delete the 3rd book (The Great Gatsby) from the dictionary
del book_authors_dict['The Great Gatsby']
print("\nDictionary after deleting the 3rd book (The Great Gatsby):", book_authors_dict)

# Print the last key-value pair in the dictionary
last_key = list(book_authors_dict.keys())[-1]
last_value = book_authors_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
