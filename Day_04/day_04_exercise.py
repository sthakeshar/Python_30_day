#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_word = 'Thirty'
second_word = 'Days'
third_word = 'Of'
fourth_word = 'Python'
full_sentence = first_word + ' ' + second_word + ' ' + third_word + ' ' + fourth_word
print(full_sentence)  # Thirty Days Of Python

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first_word = 'Coding'
second_word = 'For' 
third_word = 'All'
full_sentence = first_word + ' ' + second_word + ' ' + third_word
print(full_sentence)  # Coding For All

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print("length of company is: ", len(company))

# Change all the characters to uppercase letters using upper() method.
print("the company in uppercase is: ", company.upper())

# Change all the characters to lowercase letters using lower() method.
print("the company in lowercase is: ", company.lower())

# Use capitalize(), title(), and swapcase() methods to format the value of the string Coding For All.
print("the company capitalized is: ", company.capitalize())
print("the company in title case is: ", company.title()) 
print("the company in swapcase is: ", company.swapcase())

# Cut(slice) out the first word of Coding For All string.
first_word = company[0:6]
print("the first word is: ", first_word)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("index of 'Coding' in company is: ", company.index("Coding"))
print("find 'Coding' in company is: ", company.find("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
new_company = company.replace("Coding", "Python")
print("before replacement: ", company)  # Coding For All
print("after replacement: ", new_company)  # Python For All

# Change Python for Everyone to Python for All using the replace method or other methods.
python_everyone = "Python for Everyone"
python_all = python_everyone.replace("Everyone", "All")
print("before replacement: ", python_everyone)  # Python for Everyone
print("after replacement: ", python_all)  # Python for All

# Split the string 'Coding For All' using space as the separator (split()) .
split_company = company.split(" ")
print("split company: ", split_company)  # ['Coding', 'For', 'All']

print("the company is: ", company)
first_word = company[0:6]
print("the first word is: ", first_word)
second_word = company[7:10]
print("the second word is: ", second_word)
third_word = company[11:14]
print("the third word is: ", third_word)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = big_tech_companies.split(", ")
print("the big tech companies string is: ", big_tech_companies)
print("big tech companies: ", split_companies)

# What is the character at index 0 in the string Coding For All.
char_index_0 = company[0]
print("character at index 0 is: ", char_index_0)  # C

# What is the last index of the string Coding For All.
last_index = len(company) - 1
print("last index is: ", last_index)  # 13
print("character at last index is: ", company[-1])  # l

# What character is at index 10 in "Coding For All" string.
char_index_10 = company[10]
print("character at index 10 is: ", char_index_10)  # A

# Create an acronym or abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone"
acronym = name[0] + name[7] + name[11]
print("name is: ", name)
print("the acronym for 'Python For Everyone' is: ", acronym)  # PFE

# Create an acronym or abbreviation for the name 'Coding For All'.
acronym = company[0] + company[7] + company[11]
print("name is: ", company)
print("the acronym for '%s' is: "%company, acronym)  # CFA

# Use index to determine the position of the first occurrence of C in Coding For All.
index_of_C = company.find("C")
print("the index of first occurrence of 'C' is: ", index_of_C)  # 0
print("the index of first occurrence of 'C' is: ", company.index("C")) 

# Use index to determine the position of the first occurrence of F in Coding For All.
index_of_F = company.find("F")
print("the index of first occurrence of 'F' is: ", index_of_F)  # 7

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
index_of_l = company.rfind("l")
print("the index of last occurrence of 'l' is: ", index_of_l)  # 13

# Use index to find the position of the first occurrence of the word 'because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
index_of_because = sentence.find("because")
print("the index of first occurrence of 'because' is: ", index_of_because)  # 31

# Use rindex to find the position of the last occurrence of the word 'because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
index_of_because = sentence.rfind("because")    
print("the index of last occurrence of 'because' is: ", index_of_because)  # 47

# Slice out the phrase 'because because because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[31:54]
print("the original sentence is: ", sentence)
print("the sliced phrase is: ", phrase)  # because because because
print("the sentence after slicing is: ", sentence.replace("because"," "))  # You cannot end a sentence with is a conjunction

#Does ''Coding For All' start with a substring Coding?
print(company.startswith("coding"))

#Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence='   Coding For All      '
print(sentence.strip())

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
sentence1='30DaysOfPython'
sentence2='thirty_days_of_python'
print(sentence1.isidentifier())
print(sentence2.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result='#, '.join(python_libraries)
print(result)

#Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

#Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity\nKeshar\t24\tJapan\tTokyo")

#Use the string formatting method to display the following:
radius=10
pi=3.14
pow=2
string='radius'
print("radius=%d"%radius)
print('radius={}'.format(radius))
print("area={}*{}**{}".format(pi,string, pow))
print("The area of a circle with {} {} is {} meters square.".format(string,radius,pi*radius**pow))
print("The area of a circle with %s %d is %.2f meters square."%(string,radius,pi*radius**pow))

#Make the following using string formatting methods:
a,b=8,6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))