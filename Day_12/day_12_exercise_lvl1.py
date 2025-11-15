#Writ a function which generates a six digit/character random_user_id.
import random
import string
from random import randint

def generate_random_user_id_v2():
    """
    Generates a 6-character random ID containing letters and numbers.
    """
    characters = string.ascii_letters + string.digits
    user_id = ""
    # Loop 6 times, pick a random character, and append it
    for _ in range(6):
        user_id += random.choice(characters)
        
    return user_id

# --- Example Usage ---
print(f"Generated User ID v2: {generate_random_user_id_v2()}")
print(f"Generated User ID v2: {generate_random_user_id_v2()}")

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num1,num2=map(int, input("Enter two numbers separated by a space: ").split())
    characters = string.ascii_letters + string.digits
    
    for i in range(num2):
        user_id = ""
        for _ in range(num1):
            user_id += random.choice(characters)
        print(user_id)

user_id_gen_by_user()

def rgb_color_gen():
    print(f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})")

rgb_color_gen()