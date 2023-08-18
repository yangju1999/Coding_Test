def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])

    return parent[a]

def union(parent,a,b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def distance(a, b):
    return min(abs(a[1]-b[1]), abs(a[2]-b[2]), abs(a[3]-b[3])) 

n = int(input())
planet = []
for i in range(n):
    x,y,z = map(int, input().split())
    planet.append((i, x,y,z))

x_sorted = sorted(planet, key = lambda x:x[1])
y_sorted = sorted(planet, key = lambda x:x[2])
z_sorted = sorted(planet, key = lambda x:x[3])


# i 번째 planet pose = planet_pos[i]

parent = [i for i in range(n)]

edges = []


for i in range(n-1):
    dist = distance(x_sorted[i], x_sorted[i+1])  
    edges.append((dist, x_sorted[i][0], x_sorted[i+1][0]))

    dist = distance(y_sorted[i], y_sorted[i+1])  
    edges.append((dist, y_sorted[i][0], y_sorted[i+1][0]))

    dist = distance(z_sorted[i], z_sorted[i+1])  
    edges.append((dist, z_sorted[i][0], z_sorted[i+1][0]))

edges.sort() 

count = 0 
total_cost = 0 

for edge in edges:
    dist, a, b =edge
    if find(parent, a) == find(parent, b):
        continue 
    union(parent,a, b)
    count += 1
    total_cost += dist
    if count == n-1:
        break  

print(total_cost)






