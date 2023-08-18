import sys 
sys.setrecursionlimit(10**6)
x = int(input())

data= [0] * 30000


def f(x):
    if x ==1:
        return 0
    
    if data[x] != 0: 
        return data[x]
    
    else:
        data[x] = min(f(x//3) + (x%3) +1, f(x//5) + (x%5)+1, f(x//2) + (x%2)+1)
        return data[x]

d = [0] *30001
d[1] = 0 
def bottom_up(x):
    
    for i in range(2, x+1):
        temp = d[i-1] + 1
        if i%5 ==0:
            temp = min(temp, d[i//5]+1)
        if i%3 ==0:
            temp = min(temp, d[i//3] +1) 
        if i%2 == 0:
            temp = min(temp, d[i//2] +1)
        d[i] = temp 
    return d[x]

print(bottom_up(x))