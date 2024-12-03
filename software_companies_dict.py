# Creating a dictionary of 10 software companies and their headquarters
software_companies_dict = {
    'Microsoft': 'Redmond, Washington, USA',
    'Apple': 'Cupertino, California, USA',
    'Google': 'Mountain View, California, USA',
    'Amazon': 'Seattle, Washington, USA',
    'Facebook': 'Menlo Park, California, USA',
    'Adobe': 'San Jose, California, USA',
    'IBM': 'Armonk, New York, USA',
    'Oracle': 'Redwood City, California, USA',
    'SAP': 'Walldorf, Germany',
    'Twitter': 'San Francisco, California, USA'
}

# Print the entire dictionary
print("The entire dictionary:", software_companies_dict)

# Access and print the headquarters of the 3rd company (Google)
third_company_headquarters = list(software_companies_dict.values())[2]  # Index 2 for the 3rd item
print("\nThe headquarters of the 3rd company (Google):", third_company_headquarters)

# Update the headquarters of the 8th company (Oracle)
software_companies_dict['Oracle'] = 'Austin, Texas, USA'
print("\nUpdated headquarters of the 8th company (Oracle):", software_companies_dict['Oracle'])

# Delete the 9th company (SAP) from the dictionary
del software_companies_dict['SAP']
print("\nDictionary after deleting the 9th company (SAP):", software_companies_dict)

# Print the last key-value pair in the dictionary
last_key = list(software_companies_dict.keys())[-1]
last_value = software_companies_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
