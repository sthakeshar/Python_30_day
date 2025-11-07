#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
print(ages)
ages.sort()
print(ages)
print("the min of list is {}".format(ages[0]))
print("the max of list is {}".format(ages[-1]))

#Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[-2])
print(ages)

#Find the median age (one middle item or two middle items divided by two)
median=(len(ages))//2
print("the median of the list is {}".format(ages[median]))

#Find the average age (sum of all items divided by their number )
sum=sum(ages)
print("the average of list is {}".format(sum/len(ages)))

#Find the range of the ages (max minus min)
ages.sort()
print("the range of the ages (max minus min) is {}".format(ages[-1]-ages[0]))

#Compare the value of (min - average) and (max - average), use abs() method
averge=sum/len(ages)
print("the value of (min - average) is {}".format(abs(ages[0]-averge)))
print("the value of (max - average) is {}".format(abs(ages[-1]-averge)))