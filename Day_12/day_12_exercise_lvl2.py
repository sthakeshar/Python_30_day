#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import string
import random
from random import randint
def list_of_hexa_colors(num_colors=1):
    hex_characters = string.ascii_letters[:6] + string.digits
    generated_colors = []

    for _ in range(num_colors):
        color_code = "#"
        # A hex color code always requires exactly 6 characters after the '#'
        for _ in range(6):
            color_code += random.choice(hex_characters)
        
        generated_colors.append(color_code)
        
    return generated_colors

print(f"Single color: {list_of_hexa_colors()}")
print(f"multiple color: {list_of_hexa_colors(3)}")

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors=1):
    generated_colors = []

    for _ in range(num_colors):
        color_code = "rgb"
        for _ in range(4):
            color_code = randint(0,255),randint(0,255),randint(0,255)
        
        generated_colors.append(color_code)
        
    return generated_colors

print(f"Single color: {list_of_rgb_colors()}")
print(f"multiple color: {list_of_rgb_colors(3)}")

#Write a function generate_colors which can generate any number of hexa or rgb colors.
def  generate_colors(color,num):
    if color=='hexa':
        print(list_of_hexa_colors(num))
    if color=='rgb':
        print(list_of_rgb_colors(num))

generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']