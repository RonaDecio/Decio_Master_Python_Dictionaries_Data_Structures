# Creating a dictionary of 10 car models and their engine specifications
car_specs_dict = {
    'Toyota Corolla': '1.8L 4-Cylinder, 139 hp',
    'Honda Civic': '2.0L 4-Cylinder, 158 hp',
    'Ford Mustang': '5.0L V8, 450 hp',
    'Chevrolet Camaro': '6.2L V8, 455 hp',
    'BMW 3 Series': '2.0L 4-Cylinder Turbo, 255 hp',
    'Audi A4': '2.0L 4-Cylinder Turbo, 188 hp',
    'Mercedes-Benz C-Class': '2.0L 4-Cylinder Turbo, 255 hp',
    'Tesla Model 3': 'Electric, 283 hp',
    'Nissan Altima': '2.5L 4-Cylinder, 188 hp',
    'Volkswagen Jetta': '1.4L 4-Cylinder Turbo, 147 hp'
}

# Print the entire dictionary
print("The entire dictionary:", car_specs_dict)

# Access and print the specifications of the 4th car model (Chevrolet Camaro)
fourth_car_specs = list(car_specs_dict.values())[3]  # Index 3 for the 4th car model
print("\nThe specifications of the 4th car model (Chevrolet Camaro):", fourth_car_specs)

# Update the specifications of the 9th car model (Nissan Altima)
car_specs_dict['Nissan Altima'] = '2.5L 4-Cylinder, 190 hp'  # Updating the specifications
print("\nUpdated specifications of the 9th car model (Nissan Altima):", car_specs_dict['Nissan Altima'])

# Delete the 5th car model (BMW 3 Series) from the dictionary
del car_specs_dict['BMW 3 Series']
print("\nDictionary after deleting the 5th car model (BMW 3 Series):", car_specs_dict)

# Print the last key-value pair in the dictionary
last_key = list(car_specs_dict.keys())[-1]
last_value = car_specs_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
