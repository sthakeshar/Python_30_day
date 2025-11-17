"""Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location.
Sort out the ten most populated countries."""

import sys
import os

# Fix path so Python can import from DATA folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# Import countries data
from DATA.countries_data import countries

# 1. Sort countries by name
countries_by_name = sorted(countries, key=lambda x: x['name'])
print("Countries sorted by name:")
for country in countries_by_name[:10]:
    print(country['name'])

# 2. Sort countries by capital
countries_by_capital = sorted(countries, key=lambda x: x['capital'])
print("\nCountries sorted by capital:")
for country in countries_by_capital[:10]:
    print(f"{country['capital']} - {country['name']}")

# 3. Sort countries by population
countries_by_population = sorted(countries, key=lambda x: x['population'], reverse=True)
print("\nTop 10 most populated countries:")
for country in countries_by_population[:10]:
    print(f"{country['name']} - {country['population']}")

# 4. Get total number of unique languages
# Flatten all languages using map and for loop
all_languages = []
for country_languages in map(lambda x: x['languages'], countries):
    for lang in country_languages:
        all_languages.append(lang)

# Remove duplicates using a for loop
unique_languages = []
for lang in all_languages:
    if lang not in unique_languages:
        unique_languages.append(lang)

print("\nTotal number of unique languages:", len(unique_languages))

# 5. Find top 10 most spoken languages
# Count how many countries speak each language
language_counts = {}
for lang in unique_languages:
    count = 0
    for country_languages in map(lambda x: x['languages'], countries):
        if lang in country_languages:
            count += 1
    language_counts[lang] = count

# Sort languages by number of countries (descending)
top_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTop 10 most spoken languages:")
for lang, count in top_languages:
    print(f"{lang}: spoken in {count} countries")


