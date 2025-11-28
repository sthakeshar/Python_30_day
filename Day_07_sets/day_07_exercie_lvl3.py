age = [22, 19, 24, 25, 26, 24, 25, 24]
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age=set(age)
print(set_age)
print("length of set: ",len(set_age))
print("length of list: ",len(age))

#Explain the difference between the following data types: string, list, tuple and set

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."

lst=sentence.split(" ")
print(lst)

unique_word=set(lst)
print(unique_word)
print("the unique words in set are: ",len(unique_word))