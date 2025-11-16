#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list_in_place(lst: list) -> None:
    """
    Shuffles a list in place. Modifies the original list.
    """
    random.shuffle(lst)

def get_shuffled_list(lst: list) -> list:
    """
    Returns a new shuffled list, leaving the original list unchanged.
    """
    return random.sample(lst, len(lst))

# Example usage:
my_list = [1, 2, 3, 4, 5]

# Using shuffle_list_in_place (modifies the original list)
print(f"Original list before in-place shuffle: {my_list}")
shuffle_list_in_place(my_list)
print(f"List after in-place shuffle: {my_list}")

# Resetting the list for the next example
my_list = [1, 2, 3, 4, 5]

# Using get_shuffled_list (returns a new list)
print(f"Original list before getting a new shuffled list: {my_list}")
shuffled_new_list = get_shuffled_list(my_list)
print(f"Original list remains unchanged: {my_list}")
print(f"New shuffled list: {shuffled_new_list}")

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_unique_numbers():
    numbers = []

    while len(numbers) < 7:
        num = random.randint(0, 9)
        if num not in numbers:   # ensures uniqueness
            numbers.append(num)

    return numbers

print(seven_unique_numbers())


        