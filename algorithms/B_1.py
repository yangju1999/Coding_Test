#n,m 사이의 소수 구하기
import math

n,m = map(int, input().split())

is_prime = [True] * (1+m) 
is_prime [1] = False 

for i in range(2, int(math.sqrt(m)) +1):
    if is_prime[i] == True:
        for j in range(2, m//i+1):
            is_prime[i*j] = False 


for i in range(n, m+1):
    if is_prime[i]:
        print(i)
