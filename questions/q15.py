from collections import deque
INF = int(1e9) 


n, m, k ,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

distance[x] = 0 

q = deque() 
q.append(x)
visited[x] = True 


while q:
    now = q.popleft() 
    for naver in graph[now]:
        if visited[naver] == False:
            q.append(naver)
            visited[naver] = True
            distance[naver] = distance[now] + 1 

count = 0 
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        count += 1 
if count == 0:
    print(-1)


