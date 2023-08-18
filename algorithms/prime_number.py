import math 

def is_prime_number(n):
    root =math.floor(math.sqrt(n)) 
    for i in range(2, root+1):
        if n%i == 0:
            return False 
    return True 

print(is_prime_number(4))
print(is_prime_number(7))
