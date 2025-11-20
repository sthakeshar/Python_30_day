#Write a pattern which identifies if a string is a valid python variable
import re

def is_valid_variable(var):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(pattern, var))
# Test cases
print(is_valid_variable('first_name'))      # True
print(is_valid_variable('first-name'))      # False
print(is_valid_variable('1first_name'))     # False
print(is_valid_variable('firstname'))       # True



