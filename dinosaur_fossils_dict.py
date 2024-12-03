# Creating a dictionary of 7 dinosaurs and where their fossils were found
dinosaur_fossils_dict = {
    'Tyrannosaurus Rex': 'North America',
    'Velociraptor': 'Mongolia',
    'Triceratops': 'North America',
    'Brachiosaurus': 'Africa',
    'Stegosaurus': 'North America',
    'Allosaurus': 'North America',
    'Spinosaurus': 'North Africa'
}

# Print the entire dictionary
print("The entire dictionary:", dinosaur_fossils_dict)

# Access and print the location of the 4th dinosaur's fossils (Brachiosaurus)
fourth_dinosaur_location = list(dinosaur_fossils_dict.values())[3]  # Index 3 for the 4th dinosaur
print("\nThe location of the 4th dinosaur's fossils (Brachiosaurus):", fourth_dinosaur_location)

# Update the location of the 2nd dinosaur's fossils (Velociraptor)
dinosaur_fossils_dict['Velociraptor'] = 'China'  # Updating the location
print("\nUpdated location of the 2nd dinosaur's fossils (Velociraptor):", dinosaur_fossils_dict['Velociraptor'])

# Delete the 6th dinosaur (Allosaurus) from the dictionary
del dinosaur_fossils_dict['Allosaurus']
print("\nDictionary after deleting the 6th dinosaur (Allosaurus):", dinosaur_fossils_dict)

# Print the last key-value pair in the dictionary
last_key = list(dinosaur_fossils_dict.keys())[-1]
last_value = dinosaur_fossils_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
