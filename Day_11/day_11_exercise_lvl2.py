from collections import Counter
#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    even_count=0
    odd_count=0
    for i in range(num+1):
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    print(f"The count of all evens is {even_count}. And the count of all odds is {odd_count}.")

evens_and_odds(100)

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact=1
    if num==1 or num==0:
        return 1
    else:
        for i in range(1,num+1,1):
            fact*=i
    print(f"factorial of {num} is {fact}")

factorial(5)

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(data_structure):
    if not data_structure:
        return True
    else:
        return False

# --- Example Usage ---

my_list = []
my_string = ""
my_dict = {}
my_filled_list = [1, 2, 3]

print(f"Is my_list empty? {is_empty(my_list)}")
print(f"Is my_string empty? {is_empty(my_string)}")
print(f"Is my_dict empty? {is_empty(my_dict)}")
print(f"Is my_filled_list empty? {is_empty(my_filled_list)}")

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(data_list):
    return sum(data_list) / len(data_list)

def calculate_median(data_list):
    # Sort the list first
    sorted_list = sorted(data_list)
    n = len(sorted_list)
    
    # Check if the length is odd or even
    if n % 2 == 1:
        # Odd length: return the middle element
        return sorted_list[n // 2]
    else:
        # Even length: return the average of the two middle elements
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

def calculate_mode(data_list):
    if not data_list:
        return None

    # Count occurrences of each item
    counts = Counter(data_list)
    if not counts:
        return []

    # Find the highest frequency
    max_count = max(counts.values())
    
    # Extract all items that match the highest frequency
    modes = [item for item, count in counts.items() if count == max_count]
    return modes

def calculate_range(data_list):
    if not data_list:
        return None
    return max(data_list) - min(data_list)

def calculate_variance(data_list):
    if len(data_list) < 2:
        return None # Cannot calculate sample variance with fewer than 2 data points

    mu = calculate_mean(data_list)
    # Calculate the sum of squared differences from the mean
    squared_diffs_sum = sum([(x - mu) ** 2 for x in data_list])
    # Divide by n - 1 for sample variance
    variance = squared_diffs_sum / (len(data_list) - 1)
    return variance

def calculate_std(data_list):
    variance = calculate_variance(data_list)
    if variance is None:
        return None
    # Standard deviation is the square root of the variance
    std_dev = variance ** 0.5
    return std_dev

# --- Example Usage ---
data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5, 4, 8]

print(f"Data Set: {data}")
print(f"Mean: {calculate_mean(data):.2f}")
print(f"Median: {calculate_median(data):.2f}")
print(f"Mode(s): {calculate_mode(data)}")
print(f"Range: {calculate_range(data):.2f}")
print(f"Variance: {calculate_variance(data):.2f}")
print(f"Standard Deviation: {calculate_std(data):.2f}")

data_unimodal = [1, 2, 3, 4, 4]
print(f"\nMode of {data_unimodal}: {calculate_mode(data_unimodal)}")