n, m = map(int, input().split())

parents =[i for i in range(n+1)]
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b 

    
def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    return parents[a]


edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort(key=lambda x:x[0])

costs = []

for edge in edges:
    cost, a, b = edge 
    if find_parent(a) == find_parent(b):
        continue 
    else:
        union_parent(a,b)
        costs.append(cost)

print(sum(costs) - max(costs))




