# Creating a dictionary of 10 companies and their current CEOs
company_ceos_dict = {
    'Apple': 'Tim Cook',
    'Microsoft': 'Satya Nadella',
    'Amazon': 'Andy Jassy',
    'Google': 'Sundar Pichai',
    'Facebook': 'Mark Zuckerberg',
    'Tesla': 'Elon Musk',
    'Netflix': 'Reed Hastings',
    'Samsung': 'Kim Hyun Suk',
    'Adobe': 'Shantanu Narayen',
    'Intel': 'Pat Gelsinger'
}

# Print the entire dictionary
print("The entire dictionary:", company_ceos_dict)

# Access and print the CEO of the 6th company (Tesla)
sixth_company_ceo = list(company_ceos_dict.values())[5]  # Index 5 for the 6th item
print("\nThe CEO of the 6th company (Tesla):", sixth_company_ceo)

# Update the CEO of the 3rd company (Amazon)
company_ceos_dict['Amazon'] = 'Jeff Bezos'  # Updating CEO of Amazon
print("\nUpdated CEO of the 3rd company (Amazon):", company_ceos_dict['Amazon'])

# Delete the 9th company (Adobe) from the dictionary
del company_ceos_dict['Adobe']
print("\nDictionary after deleting the 9th company (Adobe):", company_ceos_dict)

# Print the last key-value pair in the dictionary
last_key = list(company_ceos_dict.keys())[-1]
last_value = company_ceos_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
