N, K = map(int, input().split())
from copy import deepcopy

dx = [0,0,-1,1]
dy = [1,-1,0,0]

board = []

chess_map = [[[] for _ in range(N)] for _ in range(N)] #(체스 말의 번호, direction) 튜플 정보들 저장 

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(K):
    x, y, d = map(int, input().split())
    chess_map[x-1][y-1].append([i, d-1])


def rotate_180(d):
    if d == 0:
        return 1 
    elif d == 1:
        return 0 
    elif d ==2:
        return 3 
    else:
        return 2
    
def find(index):
    for i in range(N):
        for j in range(N):
            for k in range(len(chess_map[i][j])):
                if chess_map[i][j][k][0] == index:
                    return (i,j,k)
                
def check():
    global chess_map
    for i in range(N):
        for j in range(N):
            if len(chess_map[i][j]) >= 4:
                return True 
    return False

count = 1
while count <= 1000:
    for index in range(K):
        x, y, pos = find(index)
        above_horses = deepcopy(chess_map[x][y][pos+1:]) #[(horse number, direction) ......]
        original_dir = chess_map[x][y][pos][1]
        nx = x + dx[original_dir]
        ny = y + dy[original_dir]
        if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
            new_dir = rotate_180(original_dir)
            nx = x + dx[new_dir]
            ny = y + dy[new_dir]
            if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
                chess_map[x][y][pos][1] = new_dir

            elif board[nx][ny] ==0:
                chess_map[nx][ny].append([index, new_dir])
                for horse in above_horses:
                    chess_map[nx][ny].append(horse)
                chess_map[x][y] = chess_map[x][y][:pos]

            else:
                for horse in reversed(above_horses):
                    chess_map[nx][ny].append(horse)
                chess_map[nx][ny].append([index, new_dir])
                chess_map[x][y] = chess_map[x][y][:pos]

        elif board[nx][ny] == 0: #흰색 
            chess_map[nx][ny].append([index, original_dir])
            for horse in above_horses:
                chess_map[nx][ny].append(horse)
            chess_map[x][y] = chess_map[x][y][:pos]

        else: # 빨강
            for horse in reversed(above_horses):
                chess_map[nx][ny].append(horse)
            chess_map[nx][ny].append([index, original_dir])
            chess_map[x][y] = chess_map[x][y][:pos]      

        if check() == True:
            break
    count += 1

if count > 1000:
    print(-1)
else:
    print(count)
