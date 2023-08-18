from collections import deque 

n = int(input())

graph = [[] for _ in range(n+1)]

origin_cost = [0 for _ in range(n+1)] # each cost 
cost = [0 for _ in range(n+1)] #total cost
in_degree = [0 for _ in range(n+1)]



for i in range(1,n+1):
    data = list(map(int, input().split()))
    origin_cost[i] = data[0]    
    for j in range(1, len(data)-1):
        graph[data[j]].append(i)
        in_degree[i] += 1

q = deque() 
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)
        cost[i] = origin_cost[i]


while q:
    now = q.popleft()
    for naver in graph[now]:
        if origin_cost[naver] + cost[now] > cost[naver]:
            cost[naver] = origin_cost[naver] + cost[now]

        in_degree[naver] -= 1
        if in_degree[naver] == 0:
            q.append(naver)

for i in range(1, n+1):
    print(cost[i])
    
        
        



