from itertools import combinations

L, C = map(int, input().split())
data = input().split()
data.sort() 

def count_parent(array):
    count = 0
    for a in array:
        if a in ['i','a','e', 'o', 'u']:
            count +=1 
    return count 

for candidate in combinations(data, L):
    count = count_parent(candidate)
    if count >=1 and L-count >=2: 
        print(''.join(candidate)) 


