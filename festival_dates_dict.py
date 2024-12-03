# Creating a dictionary of 10 festivals and their celebration dates
festival_dates_dict = {
    'Diwali': 'November 12, 2023',
    'Christmas': 'December 25, 2023',
    'Easter': 'April 9, 2023',
    'Halloween': 'October 31, 2023',
    'Thanksgiving': 'November 23, 2023',
    'New Year': 'January 1, 2024',
    'Lunar New Year': 'February 10, 2024',
    'Holi': 'March 25, 2024',
    'Ramadan': 'March 11, 2024',
    'Oktoberfest': 'September 21, 2024'
}

# Print the entire dictionary
print("The entire dictionary:", festival_dates_dict)

# Access and print the date of the 3rd festival (Easter)
third_festival_date = list(festival_dates_dict.values())[2]  # Index 2 for the 3rd festival
print("\nThe date of the 3rd festival (Easter):", third_festival_date)

# Update the date of the 7th festival (Lunar New Year)
festival_dates_dict['Lunar New Year'] = 'February 14, 2024'  # Updating the date
print("\nUpdated date of the 7th festival (Lunar New Year):", festival_dates_dict['Lunar New Year'])

# Delete the 5th festival (Thanksgiving) from the dictionary
del festival_dates_dict['Thanksgiving']
print("\nDictionary after deleting the 5th festival (Thanksgiving):", festival_dates_dict)

# Print the last key-value pair in the dictionary
last_key = list(festival_dates_dict.keys())[-1]
last_value = festival_dates_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
