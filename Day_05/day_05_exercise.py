#Declare an empty list
list1=list()
list2=[]

#Declare a list with more than 5 items
list1=['Apple','Banana','Cherry','Durian','Eggplant']

#Find the length of your list
print("Number of fruits are {}".format(len(list1)))

#Get the first item, the middle item and the last item of the list
print("fruits:",list1)
print("first item of list %s"%list1[0])
print("middle item of list %s"%list1[2])
print("last item of list %s"%list1[4])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Keshar',24,5.3, False,'tokyo']
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#Print the list using print()
print("list of it companies are:",it_companies)

#Print the number of companies in the list
print("the number of companies are %d"%len(it_companies))

#Print the first, middle and last company
print("It companies:",it_companies)
print("first item of list %s"%it_companies[0])
print("middle item of list %s"%it_companies[3])
print("last item of list %s"%it_companies[6])

list2=it_companies.copy()

#Print the list after modifying one of the companies
list2.pop()
list2.append("Meta")
print(list2)

#Add an IT company to it_companies
list2.insert(3,"Nvidia")

#Insert an IT company in the middle of the companies list
print(list2)
list2.insert(4,"Mercari")
print(list2)

#Change one of the it_companies names to uppercase (IBM excluded!)
upper_case=list2[-1].upper()
list2.pop()
list2.append(upper_case)
print(list2)

#Join the it_companies with a string '#;  '
print('#; '.join(list2))

#Check if a certain company exists in the it_companies list.
print('META' in list2)

#Sort the list using sort() method
print(list2)
list2.sort()
print(list2)

#Reverse the list in descending order using reverse() method
print(list2[::-1])

#Slice out the first 3 companies from the list
print(list2)
print(list2[0:3])

#Slice out the last 3 companies from the list
list3=list2[:-3]
print(list3)

#Slice out the middle IT company or companies from the list
list3.pop(2)
print(list3)
del list3[2]
print(list3)

#Remove the last IT company from the list
list3.pop()
print(list3)

#Remove all IT companies from the list
list3.clear()
print(list3)

#Destroy the IT companies list
del list2

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end+back_end
print(full_stack)

full_stack.append("Python")
full_stack.append("SQL")
full_stack.append("Redux")
print(full_stack)





