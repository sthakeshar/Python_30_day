#Write a code which gives grade to students according to theirs scores:
score=int(input("enter the score of student from 0 to 100: "))

if score>=80:
    print("the obtained grade is A")
elif score>=70:
    print("the obtained grade is B")
elif score>=60:
    print("the obtained grade is C")
elif score>=50:
    print("the obtained grade is D")
else:
    print("the obtained grade is F")

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

# Ask the user to enter a month
month = input("Enter the month: ").strip().capitalize()

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

# Print the result
print(f"The season is {season}.")

# Initial list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Ask user for a fruit name
new_fruit = input("Enter a fruit: ").strip().lower()

# Check if the fruit exists in the list
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Fruit added successfully!")
    print("Updated fruit list:", fruits)
