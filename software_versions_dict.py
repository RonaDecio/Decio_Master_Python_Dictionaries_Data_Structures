# Creating a dictionary of 6 software programs and their latest versions
software_versions_dict = {
    'Windows 11': '22H2',
    'macOS Ventura': '13.3',
    'Ubuntu': '23.04',
    'Chrome': '117.0.5938.92',
    'Firefox': '118.0.1',
    'Slack': '4.29.2'
}

# Print the entire dictionary
print("The entire dictionary:", software_versions_dict)

# Access and print the version of the 4th software (Chrome)
fourth_software_version = list(software_versions_dict.values())[3]  # Index 3 for the 4th software
print("\nThe version of the 4th software (Chrome):", fourth_software_version)

# Update the version of the 2nd software (macOS Ventura)
software_versions_dict['macOS Ventura'] = '13.4'  # Updating the version
print("\nUpdated version of the 2nd software (macOS Ventura):", software_versions_dict['macOS Ventura'])

# Delete the 5th software (Firefox) from the dictionary
del software_versions_dict['Firefox']
print("\nDictionary after deleting the 5th software (Firefox):", software_versions_dict)

# Print the last key-value pair in the dictionary
last_key = list(software_versions_dict.keys())[-1]
last_value = software_versions_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
