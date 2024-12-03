# Creating a dictionary of 10 holidays and their corresponding dates
holiday_dates_dict = {
    'New Year\'s Day': 'January 1',
    'Valentine\'s Day': 'February 14',
    'Easter': 'April 9, 2023',
    'Independence Day': 'July 4',
    'Halloween': 'October 31',
    'Thanksgiving': 'November 23, 2023',
    'Christmas': 'December 25',
    'Labor Day': 'First Monday in September',
    'Memorial Day': 'Last Monday in May',
    'Veterans Day': 'November 11'
}

# Print the entire dictionary
print("The entire dictionary:", holiday_dates_dict)

# Access and print the date of the 4th holiday (Independence Day)
fourth_holiday_date = list(holiday_dates_dict.values())[3]  # Index 3 for the 4th item
print("\nThe date of the 4th holiday (Independence Day):", fourth_holiday_date)

# Update the date of the 9th holiday (Memorial Day)
holiday_dates_dict['Memorial Day'] = 'May 29, 2023'  # Updating the date of Memorial Day
print("\nUpdated date of the 9th holiday (Memorial Day):", holiday_dates_dict['Memorial Day'])

# Delete the 2nd holiday (Valentine's Day) from the dictionary
del holiday_dates_dict['Valentine\'s Day']
print("\nDictionary after deleting the 2nd holiday (Valentine's Day):", holiday_dates_dict)

# Print the last key-value pair in the dictionary
last_key = list(holiday_dates_dict.keys())[-1]
last_value = holiday_dates_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
