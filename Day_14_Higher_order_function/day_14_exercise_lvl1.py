#Difference between map, filter, and reduce
"""map(function, iterable)

Applies a function to each element of an iterable. Returns a new iterable (map object) with transformed items.
Use it when you want to transform each element.
"""
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))   # [2, 4, 6, 8]

"""filter(function, iterable)

Applies a function that returns True/False. Keeps only the elements where the function returns True.
Use it when you want to filter elements."""

numbers = [1, 2, 3, 4]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))  # [2, 4]

"""reduce(function, iterable)
(From functools module)
Repeatedly applies a function to the iterable and reduces it to a single value.

Use it when you want to combine all elements into one output
(sum, product, maximum, etc.)"""
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)   # 10

"""Higher Order Function vs Closure vs Decorator
1. Higher-Order Function

A function that:
Takes another function as an argument, OR Returns another function.
map, filter, reduce are higher-order functions."""
def operate(func, x):
    return func(x)

print(operate(lambda x: x * 2, 5))  # 10

"""Closure
A function that remembers variables from the outer function, even after the outer function has finished executing.
"""
def outer():
    x = 10
    def inner():
        return x
    return inner

my_func = outer()
print(my_func())   # 10   (x is remembered)

"""Decorator
A function that takes another function and enhances it without modifying it.
"""
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Use for loop to print each country in the countries list.
for item in countries:
    print(item)

#Use for to print each name in the names list.
for item in names:
    print(item)

#Use for to print each number in the numbers list.
for item in numbers:
    print(item)

