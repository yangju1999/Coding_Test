from collections import deque

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

shark_pos = None
shark_size = 2 
fishs = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            data[i][j] = 0 
            shark_pos = (i, j)
        elif data[i][j] > 0:
            fishs.append((data[i][j], i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(shark_size, shark_pos, data, fishs): #물고기들 중에서 가장 가까운 물고기 정보와 그 물고기와의 거리 return 
    x_pos, y_pos = shark_pos
    q = deque() 
    q.append((x_pos, y_pos))
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    distance[x_pos][y_pos] = 0 

    while q:
        x, y=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < n and ny>=0 and ny < n:
                if data[nx][ny] <= shark_size and distance[nx][ny] == -1:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1 

    can_eat = []
    for fish in fishs:
        fish_size, fish_x, fish_y = fish 
        if fish_size < shark_size and distance[fish_x][fish_y] != -1:
            can_eat.append((distance[fish_x][fish_y], fish_x, fish_y, fish_size))

    if len(can_eat) == 0:
        return -1 
    
    can_eat.sort() 
    return can_eat[0]

                 

answer = 0
point = 0 

while fishs:
    fish_to_eat = bfs(shark_size, shark_pos, data, fishs)
 
    if fish_to_eat == -1:
        break 

    dist, x, y, size = fish_to_eat
    answer += dist
    shark_pos = (x,y)
    point += 1 
    data[x][y] = 0
    fishs.remove((size, x, y))

    if point == shark_size:
        shark_size += 1
        point = 0 


print(answer)

    
    
