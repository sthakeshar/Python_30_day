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