n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1 


x, k = map(int, input().split())

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(1,n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
             graph[start][end] = min(graph[start][end], graph[start][i] + graph[i][end])


if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
