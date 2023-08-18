import copy 
n = int(input())
data = list(map(int, input().split()))

operations = list(map(int, input().split()))

max_answer = -int(1e9)
min_answer = int(1e9)

def divide(a, b):
    if a < 0:
        return -((-a) // b)
    else:
        return a// b

def dfs(value, count, operations):
    global max_answer
    global min_answer

    if count == n:
        max_answer = max(max_answer, value)
        min_answer = min(min_answer, value)
        return 

    for i in range(4):
        
        if operations[i] > 0:
            operations[i] -= 1
            if i ==0: 
                dfs(value + data[count], count+1, operations)
            elif i == 1:
                dfs(value - data[count], count+1, operations)
            elif i == 2:
                dfs(value*data[count], count +1, operations)
            else: 
                dfs(divide(value,data[count]), count +1, operations)
            operations[i] += 1

dfs(data[0], 1, operations)
print(max_answer)
print(min_answer)


       
