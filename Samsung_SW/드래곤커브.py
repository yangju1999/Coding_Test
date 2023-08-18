n = int(input())

dragons = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]


for _ in range(n):
    dragons.append(list(map(int, input().split())))

board = [[0 for _ in range(101)] for _ in range(101)]


directions = [(0,1),(0,-1),(1,0),(-1,0)]


#이전 세대의 마지막 점이 현재 회전의 기준점이되고
#이전 세대의 처음 점이 다음 회전의 기준점이 된다 
def rotate_90(data):
    temp = []
    for i in range(len(data)-1, 0,-1):
        dir = (data[i-1][0] - data[i][0], data[i-1][1] - data[i][1])
        if dir == directions[0]:
            temp.append((-1,0))
            
        elif dir == directions[1]:
            temp.append((1,0))

        elif dir == directions[2]:
            temp.append((0,1))

        else:
            temp.append((0,-1))
    
    now = data[-1]
    for t in temp:
        nx = now[0] + t[0]
        ny = now[1] + t[1]
        now = (nx, ny)
        data.append(now)
    
    return data 


def dragon_curve(dragon):
    global board 
    x, y, d, g = dragon

    data = [(x,y), (x+dx[d], y+dy[d])]

    while g > 0:
        data=rotate_90(data)
        g-=1

    for d in data:
        if 0<=d[0]<=100 and 0<=d[1]<=100: 
            board[d[1]][d[0]] = 1

def check():
    global board
    result = 0
    for x in range(100):
        for y in range(100):
            if board[x][y] == 1 and board[x+1][y] == 1 and board[x][y+1] == 1 and board[x+1][y+1] == 1:
                result += 1

    return result 

for dragon in dragons:
    dragon_curve(dragon)

answer = check()

print(answer)

    