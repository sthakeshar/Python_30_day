import sys
sys.path.append('\\Python_30_day')

from DATA.countries import countries

for country in countries:
    if 'land' in country:
        print(country)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits=['banana', 'orange', 'mango', 'lemon']
rev_fruits=list()

for fruit in fruits:
    rev_fruits.insert(0,fruit)

print("the reversed fruit list is",rev_fruits)