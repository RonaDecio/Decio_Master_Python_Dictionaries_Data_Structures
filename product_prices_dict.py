# Creating a dictionary of 10 products and their prices
product_prices_dict = {
    'Laptop': 999.99,
    'Smartphone': 799.99,
    'Headphones': 199.99,
    'Keyboard': 49.99,
    'Mouse': 29.99,
    'Monitor': 159.99,
    'USB Drive': 19.99,
    'Webcam': 79.99,
    'Smartwatch': 249.99,
    'Speaker': 89.99
}

# Print the entire dictionary
print("The entire dictionary:", product_prices_dict)

# Access and print the price of the 4th product (Keyboard)
fourth_product_price = list(product_prices_dict.values())[3]  # Index 3 for the 4th product
print("\nThe price of the 4th product (Keyboard):", fourth_product_price)

# Update the price of the 9th product (Smartwatch)
product_prices_dict['Smartwatch'] = 259.99  # Updating the price of Smartwatch
print("\nUpdated price of the 9th product (Smartwatch):", product_prices_dict['Smartwatch'])

# Delete the 6th product (Monitor) from the dictionary
del product_prices_dict['Monitor']
print("\nDictionary after deleting the 6th product (Monitor):", product_prices_dict)

# Print the last key-value pair in the dictionary
last_key = list(product_prices_dict.keys())[-1]
last_value = product_prices_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
