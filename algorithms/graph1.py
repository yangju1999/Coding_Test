n, m = map(int, input().split())

parent = [i for i in range(n+1)]


def union(a,b):
    if find(a) < find(b):
        parent[find(b)] = find(a)
    else:
        parent[find(a)] = find(b) 
    

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


operations = []
for _ in range(m):
    operation_type, a, b = map(int, input().split())
    operations.append((operation_type, a, b))

for operation in operations:
    if operation[0] == 0:
        union(operation[1],operation[2])
    else:
        if find(operation[1]) == find(operation[2]):
            print("YES")
        else:
            print("NO")