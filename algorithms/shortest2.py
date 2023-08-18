import heapq 
import sys 

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))

distance = [INF] * (n+1)
distance[c] = 0 

pq = []
heapq.heappush(pq, (0, c))
while pq:
    dist, current = heapq.heappop(pq)
    if dist > distance[current]:
        continue 
    for neighbor in graph[current]:
        if neighbor[0] + dist < distance[neighbor[1]]:
            distance[neighbor[1]] = neighbor[0] + dist 
            heapq.heappush(pq, (distance[neighbor[1]], neighbor[1]))

total_num = 0 
total_time = 0
for i in range(1, n+1):
    if distance[i] != INF and i != c:
        total_num +=1 
        if total_time < distance[i]:
            total_time = distance[i] 

print(total_num, total_time)

