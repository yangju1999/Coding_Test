n = int(input())
data = list(map(int, input().split()))

data.sort() 

current = 0 
result = 0 

for i in range(len(data)):
    current += 1  
    if data[i] <= current:
        current = 0 
        result += 1 

print(result)

     
    
