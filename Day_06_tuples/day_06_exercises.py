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
