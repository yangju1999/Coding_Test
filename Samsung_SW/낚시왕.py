R, C, M = map(int, input().split())


#북, 남, 동, 서 
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def change_direction(d):
    if d ==0:
        return 1
    elif d ==1:
        return 0 
    elif d==2:
        return 3
    else:
        return 2



shark_map = [[0] * (C+1) for _ in range(R+1)]


for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark_map[r][c] = (s, d-1, z) 



def shark_move():
    global shark_map 
    temp_map = [[0] * (C+1) for _ in range(R+1)]
    for x in range(1, R+1):
        for y in range(1, C+1):
            if shark_map[x][y] != 0:
                speed, direction, size = shark_map[x][y]
                nx = x 
                ny = y 
                original_speed = speed 
                while speed > 0:
                    if 0<nx + dx[direction]<=R and 0<ny + dy[direction]<=C:
                        nx = nx + dx[direction]
                        ny = ny + dy[direction]
                        speed -= 1
                    else:
                        direction = change_direction(direction) 
                    
                if temp_map[nx][ny] == 0: 
                    temp_map[nx][ny] = (original_speed, direction, size)
                elif temp_map[nx][ny][2] < size:
                    temp_map[nx][ny] = (original_speed, direction, size) 

    shark_map = temp_map  
                    
total = 0 
now = 0
while now < C:
    now += 1
    for i in range(1, R+1):
        if shark_map[i][now] != 0:
            total += shark_map[i][now][2]
            shark_map[i][now] = 0 
            break 
    shark_move()

print(total)


    