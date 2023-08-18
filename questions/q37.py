n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0 

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0 

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=' ')
    print() 
     
             




 



