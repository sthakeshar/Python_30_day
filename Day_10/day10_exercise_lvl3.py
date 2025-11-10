import sys
sys.path.append('\\Python_30_day')

from DATA.countries import countries
from DATA.countries_data import countries1


for country in countries:
    if 'land' in country:
        print(country)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits=['banana', 'orange', 'mango', 'lemon']
rev_fruits=list()

for fruit in fruits:
    rev_fruits.insert(0,fruit)

print("the reversed fruit list is",rev_fruits)

#What are the total number of languages in the data


# Step 2: Create an empty set to store unique languages
unique_languages = set()

# Step 3: Loop through each country in the data
for country in countries1:
    for language in country['languages']:
        unique_languages.add(language)

# Step 4: Get the total number of unique languages
total_languages = len(unique_languages)

# Step 5: Print the result
print("Total number of unique languages:", total_languages)
