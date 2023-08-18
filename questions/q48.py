n, m, k = map(int, input().split())

space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

smell_space = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] != 0:
            smell_space[i][j] = [space[i][j], k]
# smell_space 냄새가 없으면 0, 냄새가 있으면 [상어 number, 남은 시간]
        

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_direction=list(map(int, input().split()))
shark_direction = list(map(lambda x:x-1, shark_direction))
shark_direction = [-1] + shark_direction #shark_direction[i] means i번째 shark의 direction  1부터 m까지의 shark가 있음 shark가 죽으면 -1 값 넣는 걸로 함  



direction_data =[[] for _ in range(m+1)] #i 번째 shark에 대한 방향 우선순위 정보 = shark_data[i] 

for i in range(1, m+1):
    for _ in range(4):
        direction_data[i].append(list(map(lambda x:x-1, list(map(int, input().split())))))


#index 번째 shark의 현재 위치 정보 반환
def find_shark(index):
    for i in range(n):
        for j in range(n):
            if smell_space[i][j] != 0:
                if smell_space[i][j][0] == index and smell_space[i][j][1] == k:
                    return (i, j)
    return None



def smell_decrease(smell_space):
    for i in range(n):
        for j in range(n):
            if smell_space[i][j] != 0:
                smell_space[i][j][1] -= 1
                if smell_space[i][j][1] == 0:
                    smell_space[i][j] = 0 


died_shark = 0 

def shark_move(smell_space, shark_direction):
    global died_shark

    next_shark_pos = [0 for _ in range(m+1)]
    for i in range(1, m+1):
        if find_shark(i) != None:
            x, y =find_shark(i)
            now_direction = shark_direction[i]
            next_directions = direction_data[i][now_direction]
            next_direction = None 
            for j in next_directions:
                nx = x + dx[j]
                ny = y + dy[j]
                if nx >=0 and nx < n and ny >=0 and ny< n:
                    if smell_space[nx][ny] == 0:
                        next_direction = j 
                        break 

            if next_direction == None:
                for j in next_directions:
                    nx = x + dx[j]    
                    ny = y + dy[j]
                    if nx >=0 and nx < n and ny >=0 and ny< n:
                        if smell_space[nx][ny][0] == i:
                            next_direction = j
                            break 

            nx = x + dx[next_direction]
            ny = y + dy[next_direction]
            shark_direction[i] = next_direction
            next_shark_pos[i] = [nx, ny]
    
    smell_decrease(smell_space)

    for i in range(1, m+1):
        if next_shark_pos[i] != 0:
            nx, ny = next_shark_pos[i]
            if smell_space[nx][ny] == 0:
                smell_space[nx][ny] = [i, k]

            elif smell_space[nx][ny][0] == i:
                smell_space[nx][ny] = [i, k]
            else:
                died_shark += 1
                shark_direction[i] = -1 
 
total_time = 0
    
while died_shark != m-1 and total_time < 1000:
    shark_move(smell_space, shark_direction)
    total_time += 1

if died_shark == m-1:
    print(total_time)
else:
    print(-1)
    


