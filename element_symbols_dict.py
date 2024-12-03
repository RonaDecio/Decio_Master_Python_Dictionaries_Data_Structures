# Creating a dictionary of 10 elements and their chemical symbols
element_symbols_dict = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Lithium': 'Li',
    'Beryllium': 'Be',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne'
}

# Print the entire dictionary
print("The entire dictionary:", element_symbols_dict)

# Access and print the symbol of the 6th element (Carbon)
sixth_element_symbol = list(element_symbols_dict.values())[5]  # Index 5 for the 6th item
print("\nThe symbol of the 6th element (Carbon):", sixth_element_symbol)

# Update the symbol of the 8th element (Oxygen)
element_symbols_dict['Oxygen'] = 'O2'
print("\nUpdated symbol of the 8th element (Oxygen):", element_symbols_dict['Oxygen'])

# Delete the 9th element (Fluorine) from the dictionary
del element_symbols_dict['Fluorine']
print("\nDictionary after deleting the 9th element (Fluorine):", element_symbols_dict)

# Print the last key-value pair in the dictionary
last_key = list(element_symbols_dict.keys())[-1]
last_value = element_symbols_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
