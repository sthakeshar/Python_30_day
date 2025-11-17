countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Use map to create a new list by changing each country to uppercase in the countries list
result = list(map(lambda str: str.upper(), countries))
print(result)

#Use map to create a new list by changing each number to its square in the numbers list
result=list(map(lambda x:x**2,numbers))
print(result)

#Use map to change each name to uppercase in the names list
result = list(map(lambda str: str.upper(), names))
print(result)

#Use filter to filter out countries containing 'land'.
result = list(filter(lambda str:'land' in str, countries))
print(result)

#Use filter to filter out countries having exactly six characters.
result=list(filter(lambda str:len(str)==6,countries))
print(result)

#Use filter to filter out countries containing six letters and more in the country list.
result=list(filter(lambda str:len(str)>=6,countries))
print(result)

#Use filter to filter out countries starting with an 'E'
result=list(filter(lambda str:str.startswith('E'),countries))
print(result)

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
result = reduce(
    lambda a, b: a + b,                     # step 3: sum them
    filter(
        lambda x: x % 2 == 0,               # step 2: only even numbers
        map(lambda x: x * 2, numbers)       # step 1: double numbers
    )
)
print(result)

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

print(get_string_lists([1, 'hello', True, 'world', 3.5, 'python']))

#Use reduce to sum all the numbers in the numbers list.
sum=reduce(lambda x, y:x+y,numbers)
print(sum)

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
north_european_countries=reduce(lambda x,y:f"{x}, {y}",countries[:-1])+ f" and {countries[-1]} are northen european countries"
print(north_european_countries)

import sys
import os

# Fix path so Python can import from DATA folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from DATA.countries import countries
def categorize_countries(pattern):
    return [country for country in countries if pattern.lower() in country.lower()]

print(categorize_countries("land"))
print(categorize_countries("ia"))
print(categorize_countries("stan"))
print(categorize_countries("island"))

#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def dictonary_countries():
    result={}
    for item in countries:
        first_letter = item[0].upper()     # get starting letter
        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1
    return result

print(dictonary_countries())

#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]

print(get_first_ten_countries())

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]

print(get_last_ten_countries())