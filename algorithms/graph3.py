from collections import deque
import copy 

n = int(input())

graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    for j in range(1, len(data)-1):
        graph[data[j]].append(i)
        in_degree[i] += 1


result = copy.deepcopy(time)
q = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for neighbor in graph[now]:
        in_degree[neighbor] -=1
        result[neighbor] = max(result[neighbor], result[now]+time[neighbor])
        if in_degree[neighbor] == 0:
            q.append(neighbor) 

for i in range(1, n+1):
    print(result[i])


