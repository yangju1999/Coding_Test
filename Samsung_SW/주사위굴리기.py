n, m, x, y, k = map(int, input().split())


dice = [0 for i in range(6)]

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

directions = list(map(int, input().split()))
directions = list(map(lambda x:x-1, directions))

#동, 서, 북, 남 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def turn(direction):
    a1,a2,a3,a4,a5,a6 = dice
    if direction == 0:
        dice[0] = a4
        dice[1] = a2
        dice[2] = a1
        dice[3] = a6
        dice[4] = a5
        dice[5] = a3

    elif direction == 1:
        dice[0] = a3
        dice[1] = a2
        dice[2] = a6
        dice[3] = a1
        dice[4] = a5
        dice[5] = a4
    
    elif direction ==2:
        dice[0] = a5
        dice[1] = a1
        dice[2] = a3
        dice[3] = a4
        dice[4] = a6
        dice[5] = a2

    else:
        dice[0] = a2
        dice[1] = a6
        dice[2] = a3
        dice[3] = a4
        dice[4] = a1
        dice[5] = a5


for d in directions:
    now_dx = dx[d]
    now_dy = dy[d]
    nx = x + now_dx 
    ny = y + now_dy 
    if 0<= nx < n and 0<= ny < m:
        x = nx 
        y = ny 
        turn(d)
        if data[nx][ny] == 0:
            data[nx][ny] = dice[-1]  
        else:
            dice[-1] = data[nx][ny] 
            data[nx][ny] = 0
    

        print(dice[0])



    
     

