# Creating a dictionary of 6 continents and a list of 3 countries for each
continent_countries_dict = {
    'Africa': ['Nigeria', 'Egypt', 'South Africa'],
    'Asia': ['China', 'India', 'Japan'],
    'Europe': ['Germany', 'France', 'Italy'],
    'North America': ['USA', 'Canada', 'Mexico'],
    'South America': ['Brazil', 'Argentina', 'Colombia'],
    'Australia': ['Australia', 'New Zealand', 'Papua New Guinea']
}

# Print the entire dictionary
print("The entire dictionary:", continent_countries_dict)

# Access and print the countries of the 4th continent (North America)
fourth_continent_countries = continent_countries_dict['North America']
print("\nThe countries of the 4th continent (North America):", fourth_continent_countries)

# Update the countries of the 5th continent (South America)
continent_countries_dict['South America'] = ['Chile', 'Peru', 'Venezuela']
print("\nUpdated countries of the 5th continent (South America):", continent_countries_dict['South America'])

# Delete the 6th continent (Australia) from the dictionary
del continent_countries_dict['Australia']
print("\nDictionary after deleting the 6th continent (Australia):", continent_countries_dict)

# Print the last key-value pair in the dictionary
last_key = list(continent_countries_dict.keys())[-1]
last_value = continent_countries_dict[last_key]
print("\nThe last key-value pair in the dictionary:", (last_key, last_value))
