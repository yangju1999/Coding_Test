n, m = map(int, input().split())
ice_map = []
for _ in range(n):
    ice_map.append(list(map(int, input().split())))
count= 0

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    
    if ice_map[x][y] == 0: 
        ice_map[x][y] = 1 
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True 
    else:
        return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)



