# Creating a dictionary of 8 universities and their popular courses
university_courses_dict = {
    'Harvard University': 'Computer Science',
    'Stanford University': 'Electrical Engineering',
    'Massachusetts Institute of Technology': 'Physics',
    'University of California, Berkeley': 'Biology',
    'University of Oxford': 'Law',
    'Cambridge University': 'Mathematics',
    'University of Chicago': 'Economics',
    'Princeton University': 'History'
}

# Print the entire dictionary
print("The entire dictionary:", university_courses_dict)

# Access and print the course of the 3rd university (Massachusetts Institute of Technology)
third_university_course = list(university_courses_dict.values())[2]  # Index 2 for the 3rd item
print("\nThe course of the 3rd university (Massachusetts Institute of Technology):", third_university_course)

# Update the course of the 5th university (University of Oxford)
university_courses_dict['University of Oxford'] = 'Philosophy'
print("\nUpdated course of the 5th university (University of Oxford):", university_courses_dict['University of Oxford'])

# Delete the 7th university (University of Chicago) from the dictionary
del university_courses_dict['University of Chicago']
print("\nDictionary after deleting the 7th university (University of Chicago):", university_courses_dict)

# Print the last key-value pair in the dictionary
last_key = list(university_courses_dict.keys())[-1]
last_value = university_courses_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
