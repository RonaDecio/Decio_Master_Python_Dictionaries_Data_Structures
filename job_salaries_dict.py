# Creating a dictionary of 10 jobs and their average salaries
job_salaries_dict = {
    'Software Engineer': 100000,
    'Data Scientist': 95000,
    'Product Manager': 120000,
    'Graphic Designer': 55000,
    'Accountant': 65000,
    'Teacher': 45000,
    'Nurse': 75000,
    'Web Developer': 85000,
    'Project Manager': 105000,
    'Chef': 40000
}

# Print the entire dictionary
print("The entire dictionary:", job_salaries_dict)

# Access and print the salary of the 3rd job (Product Manager)
third_job_salary = list(job_salaries_dict.values())[2]  # Index 2 for the 3rd job
print("\nSalary of the 3rd job (Product Manager):", third_job_salary)

# Update the salary of the 7th job (Nurse)
job_salaries_dict['Nurse'] = 80000
print("\nUpdated salary of the 7th job (Nurse):", job_salaries_dict['Nurse'])

# Delete the 9th job (Project Manager) from the dictionary
del job_salaries_dict['Project Manager']
print("\nDictionary after deleting the 9th job (Project Manager):", job_salaries_dict)

# Print the last key-value pair in the dictionary
last_key = list(job_salaries_dict.keys())[-1]
last_value = job_salaries_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
