n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

new_data = [[6] * (m+2) for _ in range(n+2)]
# 벽 = 6 

for i in range(n):
    for j in range(m):
        new_data[1+i][1+j] = data[i][j]

cctv = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if 0<new_data[i][j]<6:
            cctv.append((i,j, new_data[i][j]))

#북 동 남 서 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check_blind_spot(data):
    n = len(data)
    m = len(data[0])
    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                result += 1 
    return result 


answer = n*m 

def dfs(now_index):
    global answer 
    global cctv
    global new_data
    if now_index == len(cctv):
        answer = min(check_blind_spot(new_data), answer) 
        return 

    now_cctv = cctv[now_index]
    x,y,number = now_cctv

    if number == 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            changed = []
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[i]
                ny = ny + dy[i] 
            dfs(now_index +1)
            for c in changed:
                new_data[c[0]][c[1]] = 0 
        
    elif number == 2:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            changed = []
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[i]
                ny = ny + dy[i] 

            nx = x + dx[i+2]
            ny = y + dy[i+2]
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[i+2]
                ny = ny + dy[i+2] 
            
            dfs(now_index +1)
            for c in changed:
                new_data[c[0]][c[1]] = 0 

    elif number == 3:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            changed = []
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[i]
                ny = ny + dy[i] 

            nx = x + dx[(i+1)%4]
            ny = y + dy[(i+1)%4]
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[(i+1)%4]
                ny = ny + dy[(i+1)%4] 
            
            dfs(now_index +1)
            for c in changed:
                new_data[c[0]][c[1]] = 0 

    elif number == 4:
        for i in range(4):
            nx = x + dx[(i+1)%4]
            ny = y + dy[(i+1)%4]
            changed = []
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[(i+1)%4]
                ny = ny + dy[(i+1)%4] 

            nx = x + dx[(i+2)%4]
            ny = y + dy[(i+2)%4]
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[(i+2)%4]
                ny = ny + dy[(i+2)%4] 

            nx = x + dx[(i+3)%4]
            ny = y + dy[(i+3)%4]
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[(i+3)%4]
                ny = ny + dy[(i+3)%4] 

            dfs(now_index +1)
            for c in changed:
                new_data[c[0]][c[1]] = 0 


    else:
        changed = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while new_data[nx][ny] != 6:
                if new_data[nx][ny] == 0:
                    new_data[nx][ny] = 7
                    changed.append((nx,ny))
                nx = nx + dx[i]
                ny = ny + dy[i] 
            
        dfs(now_index +1)
        for c in changed:
            new_data[c[0]][c[1]] = 0 

dfs(0)
print(answer)