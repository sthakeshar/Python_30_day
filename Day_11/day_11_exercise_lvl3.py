#Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    
    # 2 and 3 are prime numbers
    if num <= 3:
        return True
    for i in range(2,(num)//2,1):
        if num%i:
            return True
        else:
            return False

print(f"Is 17 prime? {is_prime(10)}")            
        