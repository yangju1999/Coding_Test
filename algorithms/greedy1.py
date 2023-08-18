n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = 0

for i in range(m):

    if i!=0 and i%3==0:
        result += data[-2]
    else:
        result += data[-1]
    

print(result) 
    
