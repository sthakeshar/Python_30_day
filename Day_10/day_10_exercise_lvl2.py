#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for i in range(101):
    sum+=i
print("thw sum of all number between 0 to 100 is {}".format(sum))

even_sum=0
odd_sum=0
for i in range(101):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")