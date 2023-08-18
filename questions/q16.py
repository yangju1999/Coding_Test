from itertools import combinations 
from copy import deepcopy 


n, m = map(int, input().split())
data = [] 
for _ in range(n):
    data.append(list(map(int, input().split())))


area = []
virus = [] 

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            area.append((i,j))
        if data[i][j] ==2:
            virus.append((i,j)) 

 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def count_safe_area(data):
    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                result += 1
    return result 

def dfs(data, v):
    stack = [] 
    stack.append(v)
    while stack:
        x, y = stack.pop()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >=0  and new_x <n and new_y >=0 and new_y <m and data[new_x][new_y] == 0: 
                stack.append((new_x, new_y))
                data[new_x][new_y] = 2

answer = 0
for changes in list(combinations(area, 3)):
    temp_map = deepcopy(data)
    for change in changes:
        i, j = change
        temp_map[i][j] = 1

    
    for v in virus: 
        dfs(temp_map, v)

    answer = max(answer, count_safe_area(temp_map)) 

print(answer)


     
        

