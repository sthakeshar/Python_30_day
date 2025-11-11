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
