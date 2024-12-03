# Creating a dictionary of 8 flowers and their symbolic meanings
flower_meanings_dict = {
    'Rose': 'Love and passion',
    'Lily': 'Purity and refined beauty',
    'Tulip': 'Perfect love',
    'Orchid': 'Luxury and strength',
    'Daisy': 'Innocence and purity',
    'Sunflower': 'Adoration and loyalty',
    'Violet': 'Modesty and faithfulness',
    'Chrysanthemum': 'Optimism and joy'
}

# Print the entire dictionary
print("The entire dictionary:", flower_meanings_dict)

# Access and print the meaning of the 5th flower (Daisy)
fifth_flower_meaning = list(flower_meanings_dict.values())[4]  # Index 4 for the 5th item
print("\nThe meaning of the 5th flower (Daisy):", fifth_flower_meaning)

# Update the meaning of the 7th flower (Violet)
flower_meanings_dict['Violet'] = 'Humility and spirituality'  # Updating the meaning of Violet
print("\nUpdated meaning of the 7th flower (Violet):", flower_meanings_dict['Violet'])

# Delete the 6th flower (Sunflower) from the dictionary
del flower_meanings_dict['Sunflower']
print("\nDictionary after deleting the 6th flower (Sunflower):", flower_meanings_dict)

# Print the last key-value pair in the dictionary
last_key = list(flower_meanings_dict.keys())[-1]
last_value = flower_meanings_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
