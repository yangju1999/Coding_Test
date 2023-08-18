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
parent = [i for i in range(n+1)]
 
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union(parent, i+1, j+1)

trip = list(map(int, input().split()))


answer = True 
for i in range(m-1):
    if find(parent, trip[i]) != find(parent, trip[i+1]):
        answer = False 
        break 

if answer == True:
    print('YES')
else:
    print('NO')



    



    


