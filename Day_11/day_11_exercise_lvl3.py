#Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    
    # 2 and 3 are prime numbers
    if num <= 3:
        return True
    for i in range(2,(num)//2,1):
        if num%i:
            return True
        else:
            return False

print(f"Is 2 prime? {is_prime(2)}")
print(f"Is 10 prime? {is_prime(10)}")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 1 prime? {is_prime(1)}")
print(f"Is 97 prime? {is_prime(97)}")
print(f"Is 0 prime? {is_prime(0)}")
print(f"Is 100 prime? {is_prime(100)}")

#Write a functions which checks if all items are unique in the list.
def all_items_unique_no_set(input_list):
    seen_items = []
    for item in input_list:
        if item in seen_items:
            # Found a duplicate
            return False
        seen_items.append(item)
        
    # If the loop finished without finding duplicates
    return True

# --- Example Usage ---
list_unique =[1,2,3,4,5]
list_duplicates =[1,2,3,4,5,2]

print(f"List 1: {list_unique}")
print(f"Are all items unique? {all_items_unique_no_set(list_unique)}")

print(f"\nList 2: {list_duplicates}")
print(f"Are all items unique? {all_items_unique_no_set(list_duplicates)}")

#Write a function which checks if all the items of the list are of the same data type.
def all_items_same_type(input_list):
    if not input_list:
        return True
        
    # Get the data type of the first item
    first_item_type = type(input_list[0])
    
    # Iterate through the rest of the list
    for item in input_list[1:]:
        # If any item's type does not match the first item's type, return False
        if type(item) is not first_item_type:
            return False
            
    # If the loop completes without finding a different type, all items match
    return True

# --- Example Usage ---

list_homogeneous_ints =[1,2,3,4]
list_homogeneous_strings = ["cat", "dog", "bird"]
list_mixed_types = ["apple", 10, 5.5, True]
list_empty = []

print(f"List 1: {list_homogeneous_ints}")
print(f"Are all items the same type? {all_items_same_type(list_homogeneous_ints)}")

print(f"\nList 2: {list_homogeneous_strings}")
print(f"Are all items the same type? {all_items_same_type(list_homogeneous_strings)}")

print(f"\nList 3: {list_mixed_types}")
print(f"Are all items the same type? {all_items_same_type(list_mixed_types)}")

print(f"\nList 4 (empty): {list_empty}")
print(f"Are all items the same type? {all_items_same_type(list_empty)}")

#Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    # Manually defined list of Python 3.x keywords
    # This list must be updated manually if Python versions change
    PYTHON_KEYWORDS = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
        'try', 'while', 'with', 'yield'
    }

    if not isinstance(name, str):
        return False
        
    # Check syntax rules
    if not name.isidentifier():
        return False
        
    # Check if the name is in our manually defined keyword set
    if name in PYTHON_KEYWORDS:
        return False
        
    return True

# --- Example Usage ---

print(f"Is 'my_var' valid? {is_valid_variable('my_var')}")
print(f"Is 'def' valid? {is_valid_variable('def')}")
print(f"Is '1variable' valid? {is_valid_variable('1variable')}")
print(f"Is 'True' valid? {is_valid_variable('True')}")
print(f"Is 'global' valid? {is_valid_variable('global')}")

#Go to the data folder and access the countries-data.py file.
import sys
import os

# Fix path so Python can import from DATA folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from DATA.countries_data import countries
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_language():
    language_count = {}
    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

    # Get the top 10 most spoken languages
    top_10_languages = sorted_languages[:10]
    print("Top 10 most spoken languages:")
    for language, count in top_10_languages:
        print(f"{language}: {count} countries")

most_spoken_language()

#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries():
    country_population = {}
    for country in countries:
        country_population[country['name']] = country['population']

# Sort countries by population (most populated first)
    sorted_countries = sorted(country_population.items(), key=lambda x: x[1], reverse=True)
# Get the top 10 most populated countries
    top_10_populated_countries = sorted_countries[:10]

    print("\nTop 10 most populated countries:")
    for country, population in top_10_populated_countries:
        print(f"{country}: {population}")

most_populated_countries()