# total_languages.py
import sys
sys.path.append('\\Python_30_day')
# Step 1: Import the data from the correct file inside the data folder
from DATA.countries_data import countries

# Step 2: Create an empty set to store unique languages
unique_languages = set()

# Step 3: Loop through each country and collect all languages
for country in countries:
    for language in country['languages']:
        unique_languages.add(language)

# Step 4: Count total unique languages
total_languages = len(unique_languages)

# Step 5: Display results
print("Total number of unique languages:", total_languages)

#Find the ten most spoken languages from the data
language_count = {}
for country in countries:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

# Sort languages by the number of countries they are spoken in
#  Sort the dictionary by count (most spoken first)
sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

# Get the top 10 most spoken languages
top_10_languages = sorted_languages[:10]

#Find the 10 most populated countries in the world
country_population = {}
for country in countries:
    country_population[country['name']] = country['population']

# Sort countries by population (most populated first)
sorted_countries = sorted(country_population.items(), key=lambda x: x[1], reverse=True)
# Get the top 10 most populated countries
top_10_populated_countries = sorted_countries[:10]
# Display results
print("Top 10 most spoken languages:")
for language, count in top_10_languages:
    print(f"{language}: {count} countries")

print("\nTop 10 most populated countries:")
for country, population in top_10_populated_countries:
    print(f"{country}: {population}")