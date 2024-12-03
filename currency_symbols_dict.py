# Creating a dictionary of 10 currencies and their symbols
currency_symbols_dict = {
    'USD': '$',
    'EUR': '€',
    'GBP': '£',
    'JPY': '¥',
    'AUD': '$',
    'CAD': '$',
    'CHF': 'Fr.',
    'INR': '₹',
    'CNY': '¥',
    'MXN': '$'
}

# Print the entire dictionary
print("The entire dictionary:", currency_symbols_dict)

# Access and print the symbol of the 5th currency (AUD)
fifth_currency_symbol = list(currency_symbols_dict.values())[4]  # Index 4 for the 5th item
print("\nThe symbol of the 5th currency (AUD):", fifth_currency_symbol)

# Update the symbol of the 9th currency (CNY)
currency_symbols_dict['CNY'] = '元'  # Updating the symbol of the CNY currency
print("\nUpdated symbol of the 9th currency (CNY):", currency_symbols_dict['CNY'])

# Delete the 3rd currency (GBP) from the dictionary
del currency_symbols_dict['GBP']
print("\nDictionary after deleting the 3rd currency (GBP):", currency_symbols_dict)

# Print the last key-value pair in the dictionary
last_key = list(currency_symbols_dict.keys())[-1]
last_value = currency_symbols_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
