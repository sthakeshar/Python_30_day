import cmath
import math
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1,num2):
    sum=num1+num2
    return sum

num1,num2=map(int, input("Enter two numbers separated by a space: ").split())

print(f"the sum of {num1} and {num2} is  ",add_two_numbers(num1,num2))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    area=3.14*radius**2
    print(f"the area of circle having {radius} is {area}")

radius=float(input("Enter the radius of circle"))
area_of_circle(radius)

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total=0
    for i, arg in enumerate(args):
        # Check if the argument is not an integer AND not a float
        if not isinstance(arg, (int, float)):
            return f"Error: All arguments must be numbers. Argument at index {i} ('{arg}') is of type {type(arg).__name__}, which is not a valid number type."
        else:
            total += arg
    print(total)

add_all_nums(1,2,3,4,7)

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celcius):
    fahrenheit=(celcius*(9/5))+32
    return fahrenheit

print(convert_celsius_to_fahrenheit(32.5))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer
month = input("Enter the month: ").strip().capitalize()

def check_season(month):
# Determine the season
    if month in ("September", "October", "November"):
        season = "Autumn"
    elif month in ("December", "January", "February"):
        season = "Winter"
    elif month in ("March", "April", "May"):
        season = "Spring"
    elif month in ("June", "July", "August"):
        season = "Summer"
    else:
        season = "Invalid month entered"
    return season

# Print the result
print(f"The season is {check_season(month)}.")

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    else:
    # Calculate the slope: change in y / change in x
        slope = (y2 - y1) / (x2 - x1)
    return slope

# Calculate the slope for points (1, 2) and (3, 4)
slope_value = calculate_slope(1, 2, 3, 4)
print(f"The slope for points (1, 2) and (3, 4) is: {slope_value}")

# Example of an undefined slope for points (2, 3) and (2, 5)
undefined_slope_value = calculate_slope(2, 3, 2, 5)
print(f"The slope for points (2, 3) and (2, 5) is: {undefined_slope_value}")

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn
def solve_quadratic_eqn(a,b,c):
    if a == 0:
        if b == 0:
            return "No valid equation (a, b, and c are all zero or a and b are zero)"
        else:
            # Linear equation: bx + c = 0
            x = -c / b
            return (x, x) # Return as a tuple of two identical results for consistency

    # Calculate the discriminant
    delta = (b**2) - (4*a*c)

    # Use cmath.sqrt to handle both positive and negative discriminants (real and complex roots)
    # The 'cmath' module always returns a complex number, ensuring the function works universally.
    
    # Find the two solutions
    x1 = (-b - cmath.sqrt(delta)) / (2*a)
    x2 = (-b + cmath.sqrt(delta)) / (2*a)
    
    # Simplify output to real numbers if the complex part is zero
    # This makes the output cleaner for standard real-number cases
    if x1.imag == 0 and x2.imag == 0:
        x1 = x1.real
        x2 = x2.real
    return (x1, x2)    

sol1,sol2 = solve_quadratic_eqn(1, -3, 2)
print(f"Solutions for 1x^2 - 3x + 2 = 0: {sol1}, {sol2}")

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(numbers_list):
    for item in numbers_list:
        print(item)

user_data=[1,2,3,4,5]
print_list(user_data)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(input_list):
    reversed_list=[]
    for item in input_list:
        reversed_list.insert(0,item)
    
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(input_list):
    capitalize_list=[]
    for item in input_list:
        capitalize_list.append(item.capitalize())
    
    return capitalize_list

print(capitalize_list_items(['banana', 'orange', 'mango', 'lemon']))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list_name,*args):
    for item in args:
        list_name.append(item)
    return list_name

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     # [2, 3, 7, 9, 5]

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list_name,args):
    index=list_name.index(args)
    list_name.pop(index)
        

    return list_name

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum=0
    for i in range(num+1):
        sum+=i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum_odds=0
    for i in range(num+1):
        if i%2==1:
            sum_odds+=i
    return sum_odds

print(sum_of_odds(10))

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    sum_even=0
    for i in range(num+1):
        if i%2==0:
            sum_even+=i
    return sum_even

print(sum_of_even(10))