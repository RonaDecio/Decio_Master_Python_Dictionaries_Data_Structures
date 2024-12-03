# Creating a dictionary of 10 cities and their corresponding population
city_population_dict = {
    'New York': 8419600,
    'Los Angeles': 3980400,
    'Chicago': 2716000,
    'Houston': 2328000,
    'Phoenix': 1690000,
    'Philadelphia': 1584200,
    'San Antonio': 1547250,
    'San Diego': 1423851,
    'Dallas': 1341075,
    'San Jose': 1026908
}

# Print the entire dictionary
print("The entire dictionary:", city_population_dict)

# Access and print the population of the 6th city (Philadelphia)
sixth_city_population = list(city_population_dict.values())[5]  # Index 5 for the 6th item
print("\nThe population of the 6th city (Philadelphia):", sixth_city_population)

# Update the population of the 3rd city (Chicago)
city_population_dict['Chicago'] = 2800000
print("\nUpdated population of the 3rd city (Chicago):", city_population_dict['Chicago'])

# Delete the 9th city (Dallas) from the dictionary
del city_population_dict['Dallas']
print("\nDictionary after deleting the 9th city (Dallas):", city_population_dict)

# Print the last key-value pair in the dictionary
last_key = list(city_population_dict.keys())[-1]
last_value = city_population_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
