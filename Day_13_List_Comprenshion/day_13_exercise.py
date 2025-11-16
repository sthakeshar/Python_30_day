#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [i for i in numbers if i>=0]  
print(positive_numbers)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = []

for outer in list_of_lists:       # e.g. [[1,2,3]]
    for inner in outer:           # e.g. [1,2,3]
        for num in inner:         # e.g. 1,2,3
            flat_list.append(num)

print(flat_list)   # [1,2,3,4,5,6,7,8,9]

flat_list = [num 
             for outer in list_of_lists
             for inner in outer
             for num in inner]

print(flat_list)   # [1,2,3,4,5,6,7,8,9]

#Using list comprehension create the following list of tuples:
result1 = [
    (i, 1, i**1, i**2, i**3, i**4, i**5)
    for i in range(11)
]

for row in result1:
    print(row)

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
result2 = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for [(country, capital)] in countries
]

print(result2)

#Change the following list to a list of dictionaries:
#countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

result3=[
    {'country':country,'city':capital}
    for [(country, capital)] in countries
]
print(result3)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
result4=[
    first_name+" "+last_name
    for [(first_name,last_name)] in names
]

print(result4)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
slope=lambda x1,y1,x2,y2:(y2-y1)/(x2-x1)
y_intercept=lambda x1,y1,x2,y2:(((y2-y1)/(x2-x1))*x2)-y2
print(slope(2,4,4,5))
print(y_intercept(2,4,4,5))