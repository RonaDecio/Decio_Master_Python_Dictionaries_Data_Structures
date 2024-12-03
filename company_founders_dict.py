# Creating a dictionary of 8 companies and their founders
company_founders_dict = {
    'Apple': 'Steve Jobs',
    'Microsoft': 'Bill Gates',
    'Tesla': 'Elon Musk',
    'Amazon': 'Jeff Bezos',
    'Facebook': 'Mark Zuckerberg',
    'Google': 'Larry Page and Sergey Brin',
    'Twitter': 'Jack Dorsey',
    'SpaceX': 'Elon Musk'
}

# Print the entire dictionary
print("The entire dictionary:", company_founders_dict)

# Access and print the founder of the 6th company (Google)
sixth_company_founder = list(company_founders_dict.values())[5]  # Index 5 for the 6th company
print("\nThe founder of the 6th company (Google):", sixth_company_founder)

# Update the founder of the 2nd company (Microsoft)
company_founders_dict['Microsoft'] = 'Paul Allen'  # Updating the founder
print("\nUpdated founder of the 2nd company (Microsoft):", company_founders_dict['Microsoft'])

# Delete the 8th company (SpaceX) from the dictionary
del company_founders_dict['SpaceX']
print("\nDictionary after deleting the 8th company (SpaceX):", company_founders_dict)

# Print the last key-value pair in the dictionary
last_key = list(company_founders_dict.keys())[-1]
last_value = company_founders_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
