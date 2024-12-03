# Create a dictionary of 8 foods and their recipes
food_recipes_dict = {
    'Pizza': 'Dough, tomato sauce, cheese, toppings of your choice',
    'Pasta': 'Pasta, olive oil, garlic, tomatoes, basil, parmesan',
    'Burger': 'Beef patty, lettuce, tomato, cheese, burger bun',
    'Sushi': 'Rice, nori (seaweed), fish, wasabi, soy sauce',
    'Tacos': 'Taco shells, ground beef, lettuce, cheese, salsa, sour cream',
    'Salad': 'Lettuce, tomatoes, cucumber, olive oil, vinegar',
    'Fried Rice': 'Rice, eggs, soy sauce, peas, carrots, onions',
    'Pancakes': 'Flour, eggs, milk, sugar, butter, syrup'
}

# Print the entire dictionary
print("The entire dictionary:")
print(food_recipes_dict)

# Access and print the recipe of the 5th food (Tacos)
fifth_food_recipe = list(food_recipes_dict.values())[4]  # Index 4 for the 5th food
print("\nRecipe of the 5th food (Tacos):", fifth_food_recipe)

# Update the recipe of the 3rd food (Burger)
food_recipes_dict['Burger'] = 'Beef patty, lettuce, tomato, bacon, cheese, burger bun'
print("\nUpdated recipe of the 3rd food (Burger):", food_recipes_dict['Burger'])

# Delete the 7th food (Fried Rice) from the dictionary
del food_recipes_dict['Fried Rice']
print("\nDictionary after deleting the 7th food (Fried Rice):")
print(food_recipes_dict)

# Print the last key-value pair in the dictionary
last_key = list(food_recipes_dict.keys())[-1]
last_value = food_recipes_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
