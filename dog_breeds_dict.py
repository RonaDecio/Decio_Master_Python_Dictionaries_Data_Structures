# Creating a dictionary of 10 dog breeds and their sizes
dog_breeds_dict = {
    'Chihuahua': 'Small',
    'Beagle': 'Medium',
    'Labrador Retriever': 'Large',
    'German Shepherd': 'Large',
    'Bulldog': 'Medium',
    'Poodle': 'Medium',
    'Golden Retriever': 'Large',
    'Cocker Spaniel': 'Medium',
    'Boxer': 'Large',
    'Dachshund': 'Small'
}

# Print the entire dictionary
print("The entire dictionary:", dog_breeds_dict)

# Access and print the size of the 5th breed (Bulldog)
fifth_breed_size = list(dog_breeds_dict.values())[4]  # Index 4 for the 5th breed
print("\nThe size of the 5th breed (Bulldog):", fifth_breed_size)

# Update the size of the 8th breed (Cocker Spaniel)
dog_breeds_dict['Cocker Spaniel'] = 'Small'  # Updating the size
print("\nUpdated size of the 8th breed (Cocker Spaniel):", dog_breeds_dict['Cocker Spaniel'])

# Delete the 6th breed (Poodle) from the dictionary
del dog_breeds_dict['Poodle']
print("\nDictionary after deleting the 6th breed (Poodle):", dog_breeds_dict)

# Print the last key-value pair in the dictionary
last_key = list(dog_breeds_dict.keys())[-1]
last_value = dog_breeds_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
