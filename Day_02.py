
# Variables in Python

first_name = 'Keshar'
middle_name='Narayan'
last_name = 'Shrestha'
country = 'Japan'
city = 'Tokyo'
age = 24
is_married = False
skills = ['HTML', 'CSS', 'JS', 'Vue', 'Python']
person_info = {
    'firstname':'Keshar',
    'middlename':'Narayan', 
    'lastname':'Yetayeh', 
    'country':'Japan',
    'city':'tokyo'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Middle Name:',middle_name)
print('Middle Name Length:',len(middle_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name,middle_name, last_name, country, age, is_married = 'Keshar', 'Narayan','Shrestha', 'Japan', 24, False

print(first_name, middle_name,last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)