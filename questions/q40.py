import heapq 

n, m = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
distance = [INF for _ in range(n+1)]

distance[1] = 0 
q = [] 
heapq.heappush(q, (0, 1))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue 

    for naver in graph[now]:
        if dist + 1 < distance[naver]:
            distance[naver] = dist + 1
            heapq.heappush(q, (distance[naver], naver))
 
answer = max(distance[1:])
index = []

for i in range(1, n+1):
    if distance[i] == answer:
        index.append(i)  

print(index[0], answer, len(index))


    

    