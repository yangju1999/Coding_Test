import heapq

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

n, m = map(int, input().split())

parent = [i for i in range(n)]

q = []

total_cost = 0 

for _ in range(m):
    x, y, z = map(int, input().split())
    total_cost += z 
    heapq.heappush(q, (z,x,y))

count = 0
saved_cost = 0

while count != n-1:
    cost, x, y =heapq.heappop(q)
    if find(parent, x) == find(parent, y):
        continue 
    union(parent, x, y)
    count += 1
    saved_cost += cost 


print(total_cost - saved_cost)


    