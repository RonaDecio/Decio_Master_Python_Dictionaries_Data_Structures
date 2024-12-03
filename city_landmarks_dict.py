# Creating a dictionary of 8 cities and their famous landmarks
city_landmarks_dict = {
    'Paris': 'Eiffel Tower',
    'New York': 'Statue of Liberty',
    'Rome': 'Colosseum',
    'London': 'Big Ben',
    'Tokyo': 'Tokyo Tower',
    'Cairo': 'Pyramids of Giza',
    'Sydney': 'Sydney Opera House',
    'Beijing': 'Great Wall of China'
}

# Print the entire dictionary
print("The entire dictionary:", city_landmarks_dict)

# Access and print the landmark of the 6th city (Cairo)
sixth_city_landmark = list(city_landmarks_dict.values())[5]  # Index 5 for the 6th city
print("\nThe landmark of the 6th city (Cairo):", sixth_city_landmark)

# Update the landmark of the 2nd city (New York)
city_landmarks_dict['New York'] = 'Empire State Building'  # Updating the landmark
print("\nUpdated landmark of the 2nd city (New York):", city_landmarks_dict['New York'])

# Delete the 7th city (Sydney) from the dictionary
del city_landmarks_dict['Sydney']
print("\nDictionary after deleting the 7th city (Sydney):", city_landmarks_dict)

# Print the last key-value pair in the dictionary
last_key = list(city_landmarks_dict.keys())[-1]
last_value = city_landmarks_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
