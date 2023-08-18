n, m = map(int, input().split())

graph = [[False for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = True

for i in range(1, n+1):
    graph[i][i] = True 

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True 

answer = [0 for _ in range(n+1)]

for i in range(1, n+1):
     for j in range(1, n+1):
         
        if graph[i][j] == True and i != j:
            answer[i] += 1
            answer[j] += 1

count = 0 
for i in range(1, n+1):
    if answer[i] == n-1:
        count += 1
        
print(count) 


    
