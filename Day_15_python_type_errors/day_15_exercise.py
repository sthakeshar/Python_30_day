#-----syntax error-----
"""
print 'hello world'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"""

#---Name error----
"""
print(age)
NameError: name 'age' is not defined
"""

#-----IndexError-----
"""
numbers = [1, 2, 3, 4, 5]
numbers[5]
IndexError: list index out of range
"""

#----ModuleNotFoundError----
"""
import maths    
ModuleNotFoundError: No module named 'maths'
"""

#-----AttributeError----
"""
import math
math.PI
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
"""

#----KeyError----
"""
users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['name']
'Asab'
users['county']
KeyError: 'county'
"""

#----TypeError---
"""
4 + '3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

#----ImportError----
"""
from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)
"""

#-----ValueError---
"""
int('12a')
ValueError: invalid literal for int() with base 10: '12a'
"""

#-----ZeroDivisionError----
"""
1/0
ZeroDivisionError: division by zero
"""