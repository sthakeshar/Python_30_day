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

