from collections import deque 

n, l, r = map(int, input().split())

data = [] 
for _ in range(n):
    data.append(list(map(int, input().split())))


count = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check():
    for i in range(n):
        for j in range(n):
            now = data[i][j]
            for k in range(4):
                new_x = i + dx[k]
                new_y = j + dy[k]
                if new_x >= 0 and new_x < n and new_y >=0 and new_y <n:
                    if l <= abs(now - data[new_x][new_y]) <= r: 
                        return True 
    return False 

def bfs(x, y,group):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        now = data[x][y]
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if new_x >= 0 and new_x < n and new_y >=0 and new_y <n:
                if group[new_x][new_y] != (new_x, new_y):
                    continue
                if l <= abs(now - data[new_x][new_y]) <= r:
                    group[new_x][new_y] = group[x][y]
                    q.append((new_x, new_y))
    

def population_move(group):
    group_data = {}
    for x in range(n):
        for y in range(n):
            if group[x][y] not in group_data:
                group_data[group[x][y]] = [data[x][y]]
            else:
                group_data[group[x][y]].append(data[x][y])
    for key in group_data.keys():
        group_data[key] = sum(group_data[key])//len(group_data[key])
    for x in range(n):
        for y in range(n):
            data[x][y] = group_data[group[x][y]] 
            



while True:
    if not check():
        break 
        
    count += 1
    group = [[(x,y) for y in range(n)] for x in range(n)]


    for x in range(n):
        for y in range(n):
            bfs(x, y,group)

    population_move(group)


     
                
print(count)   
    