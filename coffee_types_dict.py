# Creating a dictionary of 10 types of coffee and their descriptions
coffee_types_dict = {
    'Espresso': 'A strong, black coffee brewed by forcing hot water through finely-ground coffee beans.',
    'Americano': 'A diluted espresso, made by adding hot water to espresso, resulting in a less intense flavor.',
    'Latte': 'A coffee drink made with espresso and steamed milk, topped with a small amount of foam.',
    'Cappuccino': 'A coffee drink made with equal parts espresso, steamed milk, and milk foam.',
    'Macchiato': 'An espresso with a small amount of steamed milk, leaving a "stain" or "mark" on the coffee.',
    'Mocha': 'A coffee drink made with espresso, steamed milk, and chocolate syrup or cocoa powder.',
    'Flat White': 'A coffee drink made with espresso and steamed milk, similar to a latte but with a higher ratio of coffee to milk.',
    'Affogato': 'A dessert coffee made by pouring hot espresso over a scoop of vanilla ice cream.',
    'Cortado': 'A coffee drink made with equal parts espresso and warm milk, typically served in a small glass.',
    'Irish Coffee': 'A cocktail made with hot coffee, Irish whiskey, sugar, and topped with cream.'
}

# Print the entire dictionary
print("The entire dictionary:", coffee_types_dict)

# Access and print the description of the 4th type of coffee (Cappuccino)
fourth_coffee_description = list(coffee_types_dict.values())[3]  # Index 3 for the 4th type
print("\nDescription of the 4th type of coffee (Cappuccino):", fourth_coffee_description)

# Update the description of the 8th type of coffee (Affogato)
coffee_types_dict['Affogato'] = 'A dessert made by pouring hot espresso over a scoop of ice cream or gelato.'
print("\nUpdated description of the 8th type of coffee (Affogato):", coffee_types_dict['Affogato'])

# Delete the 5th type of coffee (Macchiato) from the dictionary
del coffee_types_dict['Macchiato']
print("\nDictionary after deleting the 5th type of coffee (Macchiato):", coffee_types_dict)

# Print the last key-value pair in the dictionary
last_key = list(coffee_types_dict.keys())[-1]
last_value = coffee_types_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
