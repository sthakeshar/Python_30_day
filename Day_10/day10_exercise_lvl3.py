import sys
sys.path.append('D:\\KESHAR\\Python_30_day')

from DATA.countries import countries
from DATA import countries_data


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
