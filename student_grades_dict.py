# Create a dictionary of 5 students and their corresponding grades
student_grades_dict = {
    'Student1': 'B',
    'Student2': 'C',
    'Student3': 'A',
    'Student4': 'B',
    'Student5': 'D'
}

# Print the entire dictionary
print("Student Grades Dictionary:", student_grades_dict)

# Access and print the grade of the 3rd student
print("Grade of third student:", student_grades_dict['Student3'])

# Update the grade of the 2nd student
student_grades_dict['Student2'] = 'A'

# Print updated dictionary
print("Updated Student Grades Dictionary:", student_grades_dict)

# Delete the entry of the 5th student
del student_grades_dict['Student5']

# Print updated dictionary after deletion
print("Dictionary after deleting Student5:", student_grades_dict)

# Print the last key-value pair in the dictionary
last_key = list(student_grades_dict.keys())[-1]
last_value = student_grades_dict[last_key]
print(f"Last key-value pair in the dictionary: {last_key}: {last_value}")
