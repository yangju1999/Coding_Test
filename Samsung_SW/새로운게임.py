N, K = map(int, input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]
board = []

status = [[[] for _ in range(N)] for _ in range(N)]

chess = [] # i번째 말 -> chess[i-1]

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(K):
    x, y, d = map(int, input().split())
    chess.append((x-1,y-1,d-1,0))
    status[x-1][y-1].append(i)


def rotate_180(d):
    if d == 0:
        return 1 
    elif d == 1:
        return 0 
    elif d ==2:
        return 3 
    else:
        return 2
    
def reverse(arr):
    result = []
    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
    return result


def check():
    global status
    for i in range(N):
        for j in range(N):
            if len(status[i][j]) >= 4:
                return True 
    return False

def move():
    global board 
    global status 
    global chess
    global count 

    for i in range(len(chess)):
        x,y,dir,pos = chess[i]
        now_horses = status[x][y] # 현재 i 번째 체스말과 함께 있는 말들(i번째 체스 말도 포함)
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
            dir = rotate_180(dir)
            nx = x + dx[dir] 
            ny = y + dy[dir] 
            if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
                chess[i] = (x,y,dir,pos)

            elif board[nx][ny] == 1: #빨강
                length = len(status[nx][ny])
                status[nx][ny] += reverse(now_horses[pos:])
                if len(status[nx][ny]) >=4:
                    print(count)
                    exit() 

                chess[i] =(nx,ny,dir,length + len(now_horses)-1) #변경된 dir 때문에 따로 처리해야 함  
                for horse in now_horses[pos+1:]:
                    chess[horse] = (nx, ny, chess[horse][2], length+ len(now_horses) + pos -chess[horse][3]-1)
                status[x][y] = now_horses[:pos]

                
            else: #흰색
                length = len(status[nx][ny])
                status[nx][ny] += now_horses[pos:]
                if len(status[nx][ny]) >=4:
                    print(count)
                    exit()
                chess[i] =(nx,ny,dir,length)
                for horse in now_horses[pos+1:]:
                    chess[horse] = (nx, ny, chess[horse][2], length+chess[horse][3]-pos)
                status[x][y] = now_horses[:pos]
                
                    

        elif board[nx][ny] == 1:
            length = len(status[nx][ny])
            status[nx][ny] += reverse(now_horses[pos:])
            if len(status[nx][ny]) >=4:
                print(count)
                exit()

            for horse in now_horses[pos:]:
                chess[horse] = (nx, ny, chess[horse][2], length+ len(now_horses) + pos -chess[horse][3]-1)
            status[x][y] = now_horses[:pos]

        else: #board[nx][ny] == 0
            length = len(status[nx][ny])
            status[nx][ny] += now_horses[pos:]
            if len(status[nx][ny]) >=4:
                print(count)
                exit() 
            for horse in now_horses[pos:]:
                chess[horse] = (nx, ny, chess[horse][2], length+chess[horse][3]-pos)
            status[x][y] = now_horses[:pos]
        if check() == True:
            print(count)
            exit() 

count = 0

while count <= 1000:
    count += 1
    move()

if count > 1000:
    print(-1)
    


