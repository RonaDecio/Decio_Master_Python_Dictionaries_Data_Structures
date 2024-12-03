# Creating a dictionary of 10 phone models and their manufacturers
phone_models_dict = {
    'iPhone 15': 'Apple',
    'Galaxy S23': 'Samsung',
    'Pixel 8': 'Google',
    'OnePlus 11': 'OnePlus',
    'Xperia 1 IV': 'Sony',
    'Moto G Power': 'Motorola',
    'Redmi Note 12': 'Xiaomi',
    'Galaxy Z Fold 5': 'Samsung',
    'Nokia G400': 'Nokia',
    'Huawei P60': 'Huawei'
}

# Print the entire dictionary
print("The entire dictionary:", phone_models_dict)

# Access and print the manufacturer of the 2nd phone model (Galaxy S23)
second_phone_manufacturer = list(phone_models_dict.values())[1]  # Index 1 for the 2nd phone model
print("\nThe manufacturer of the 2nd phone model (Galaxy S23):", second_phone_manufacturer)

# Update the manufacturer of the 8th phone model (Galaxy Z Fold 5)
phone_models_dict['Galaxy Z Fold 5'] = 'Samsung Electronics'  # Updating the manufacturer
print("\nUpdated manufacturer of the 8th phone model (Galaxy Z Fold 5):", phone_models_dict['Galaxy Z Fold 5'])

# Delete the 6th phone model (Moto G Power) from the dictionary
del phone_models_dict['Moto G Power']
print("\nDictionary after deleting the 6th phone model (Moto G Power):", phone_models_dict)

# Print the last key-value pair in the dictionary
last_key = list(phone_models_dict.keys())[-1]
last_value = phone_models_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
