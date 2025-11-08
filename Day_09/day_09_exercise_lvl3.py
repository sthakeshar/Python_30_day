person={
    'first_name': 'keshar',
    'last_name': 'shrestha',
    'age': 24,
    'country': 'Japan',
    'is_marred': False,
    'skills': ['JavaScript', 'HTML', 'CSS', 'Mysql', 'Python'],
    'address': {
        'street': 'kamakura katsushika 3-35-12',
        'zipcode': '1250053'
    }
    }

if 'skills' in person:
    skills=person['skills']
    middle_index=len(skills)//2
    middle_skills=skills[middle_index]
    print("the middle skill in person is {} ".format(middle_skills))
else:
    print("The person dictionary has no 'skills' key.")

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    skill=person['skills']
    if 'Python' in skill:
        print("the person has python skill")
    else:
        print("the person doesnt have skill python")
else:
    print("person dosent have skills key")

#If the person is married and if he lives in Finland, print the information in the following format:
is_married=person['is_marred']
country=person['country']

print(country)
print(is_married)
if is_married and country=='Finland':
    print("Asabeneh Yetayeh lives in Finland. He is married.")
else:
    print("Asabeneh Yetayeh doesnt lives in Finland. He is married.")
