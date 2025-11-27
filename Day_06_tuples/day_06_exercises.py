#Create an empty tuple
tup=tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers=('Dhana','Binod')
sisters=('anu','sarina')

#Join brothers and sisters tuples and assign it to siblings
siblings=brothers+sisters

#How many siblings do you have?
siblings_count=len(siblings)
print("the no. of sibillings are: ",siblings_count)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members=('Lila','Sita')+siblings
print(family_members)

#Unpack siblings and parents from family_members
print("the siblings are: ",family_members[-4:])

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Apple','Banana','Cherry')
vegetables=('Eggplant','Potato')
animal_products=('chicken','Beef','Pork')

food_stuffs_tp=fruits+vegetables+animal_products
print(food_stuffs_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuffs_lt=list(food_stuffs_tp)
print(food_stuffs_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print('the sliced out item are: ',food_stuffs_lt[3:6])

#Slice out the first three items and the last three items from food_staff_lt list
print("the first three items are: ",food_stuffs_lt[:3])
print("the last three items are: ",food_stuffs_lt[-3:])

#Delete the food_staff_tp tuple completely
del food_stuffs_tp

#Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'estonia' in nordic_countries:
    print(True)
else:
    print(False)
# Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print(True)
else:
    print(False)