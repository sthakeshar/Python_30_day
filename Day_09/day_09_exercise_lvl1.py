#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age=int(input("Enter your age: ") )
if age >18:
    print('You are old enough to drive')
else:
    print('You need {} more year to drive'.format(18-age))

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
my_age=24
your_age=age

if my_age>your_age:
    print("I am {} years older than you".format(my_age-your_age))
else:
    print("You are {} years older than me".format(your_age-my_age))

    
#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
number_one=int(input("Enter number one: "))
number_two=int(input("Enter number two: "))

if number_one>number_two:
    print("{} is greater than {}".format(number_one,number_two))
else:
    print("{} is greater than {}".format(number_two,number_one))