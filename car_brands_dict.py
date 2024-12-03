# Creating a dictionary of 10 car brands and their country of origin
car_brands_dict = {
    'Toyota': 'Japan',
    'BMW': 'Germany',
    'Ford': 'USA',
    'Chevrolet': 'USA',
    'Audi': 'Germany',
    'Honda': 'Japan',
    'Hyundai': 'South Korea',
    'Nissan': 'Japan',
    'Kia': 'South Korea',
    'Ferrari': 'Italy'
}

# Print the entire dictionary
print("The entire dictionary:", car_brands_dict)

# Access and print the country of origin of the 3rd car brand (Ford)
third_car_country = list(car_brands_dict.values())[2]  # Index 2 for the 3rd item
print("\nThe country of origin of the 3rd car brand (Ford):", third_car_country)

# Update the country of origin of the 7th car brand (Hyundai)
car_brands_dict['Hyundai'] = 'South Korea (Updated)'
print("\nUpdated country of origin of the 7th car brand (Hyundai):", car_brands_dict['Hyundai'])

# Delete the 8th car brand (Nissan) from the dictionary
del car_brands_dict['Nissan']
print("\nDictionary after deleting the 8th car brand (Nissan):", car_brands_dict)

# Print the last key-value pair in the dictionary
last_key = list(car_brands_dict.keys())[-1]
last_value = car_brands_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
