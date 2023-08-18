n, m = map(int, input().split())
x, y, d = map(int, input().split())

room = []

for _ in range(n):
    room.append(list(map(int, input().split())))

#북, 동, 남, 서 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[False for _ in range(m)] for _ in range(n)]


def rotate_90(direction):
    return (direction -1) % 4 

count = 0

while True:
    if visited[x][y] == False:
        visited[x][y] = True 
        count += 1
    
    exist = False 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if room[nx][ny] != 1 and visited[nx][ny] == False:
            exist = True 

    if exist == False:
        nx = x - dx[d]
        ny = y - dy[d]
        if room[nx][ny] == 1:
            break 
        else:
            x = nx 
            y = ny 
    else:
        d = rotate_90(d)
        nx = x + dx[d]
        ny = y + dy[d]
        if room[nx][ny] != 1 and visited[nx][ny] == False:
            x = nx 
            y = ny 

print(count)  

    