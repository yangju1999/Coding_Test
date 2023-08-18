#1부터 n까지 모든 소수 출력 

import math 

n = int(input())
is_prime = [True for _ in range(n+1)]
is_prime[0] = False 
is_prime[1] = False 

root = int(math.sqrt(n))
for i in range(2, root+1):
    if is_prime[i] == True:
        temp = n//i
        for j in range(2, temp+1):
            is_prime[i*j] = False

for i in range(2, n+1):
    if is_prime[i] == True:
        print(i, end=' ')
      


        
    