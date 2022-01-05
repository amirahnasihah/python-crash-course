''' Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'. '''

major = {
	'nile': 'egypt', 
	'ganges': 'india', 
	'danube': 'europe'
	}

for river, country in major.items():
	print(f"The {river.title()} runs through {country.title()}.\n")

# loop each river
for river in major.keys():
	print(f"- {river.upper()}")

print('\n')

# loop each country
for country in major.values():
	print(country.title())


# own experiment
print('\n')

for river in set(major.values()):		# set() = unique
	print(river.title())

for x in sorted(major.keys()):		# sorted() = alphabetical order
	print(x.upper())



# Matt answer

print('\n\n\nMatt answer:')


rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")