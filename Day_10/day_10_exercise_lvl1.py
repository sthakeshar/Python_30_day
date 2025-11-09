#Iterate 0 to 10 using for loop, do the same using while loop.
#using for loop
print("printing 0 to 10 using for loop")
for i in range(11):
    print(i)

#using while
print("\n printing 0 to 10 using while loop")
i=0
while i<=10:
    print(i)
    i+=1

#Iterate 10 to 0 using for loop, do the same using while loop.
print("\n printing  10 to 0 using for loop")
numbers=list(range(11))
numbers.reverse()
for i in numbers:
    print(i)

print("\n printing  10 to 0 using while loop")
i=10
while i>=0:
    print(i)
    i-=1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
numbers=[1,2,3,4,5,6,7]

for i in numbers:
    print("# "*i)

#Use nested loops to create the following:
print("\n")
for i in numbers:
    for j in numbers:
        print("#", end=" ")
    print()

#Print the following pattern:
print("\n")
for i in range(11):
        print("{} * {}= {}".format(i,i,i*i))

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
python_framework=['Python', 'Numpy','Pandas','Django', 'Flask']
for item in python_framework:
     print(item)

#Use for loop to iterate from 0 to 100 and print only even numbers
print("\nthe even numbers from 0 to 100 are:")
for item in range(101):
     if item%2==0:
          print(item, end=" ")

#Use for loop to iterate from 0 to 100 and print only odd numbers
print("\nthe odd numbers from 0 to 100 are:")
for item in range(101):
     if item%2!=0:
          print(item, end=" ")

