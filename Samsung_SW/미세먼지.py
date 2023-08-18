n, m, T = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

air_cleaner = []

for i in range(n):
    if room[i][0] == -1:
        air_cleaner.append(i)


dx = [1,-1,0,0]
dy = [0,0,1,-1]


def rotate_up(start):
    global room 
    for i in range(start-2, -1, -1):
        room[i+1][0] = room[i][0]
    for j in range(1,m):
        room[0][j-1] = room[0][j]
    for i in range(1,start+1):
        room[i-1][m-1] = room[i][m-1]
    for j in range(m-2, 0, -1):
        room[start][j+1] = room[start][j]
    room[start][1] = 0 
    
def rotate_down(start):
    global room 
    for i in range(start +2, n):
        room[i-1][0] = room[i][0] 
    for j in range(1, m):
        room[n-1][j-1] = room[n-1][j]
    for i in range(n-1, start, -1):
        room[i][m-1] = room[i-1][m-1]
    for j in range(m-2, 0, -1):
        room[start][j+1] = room[start][j]
    room[start][1] = 0 


def air_clean():
    global room 
    global air_cleaner
    up, down = air_cleaner
    rotate_up(up)
    rotate_down(down)
    

def dust_move():
    global room 
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if room[x][y] >= 5: 
                value = room[x][y]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i] 
                    if 0<=nx<n and 0<=ny<m:
                        if room[nx][ny] != -1:
                            temp[nx][ny] += value//5
                            room[x][y] -= value//5
    for i in range(n):
        for j in range(m):
            room[i][j] += temp[i][j] 

                        
def good_print(room):
    for i in range(n):
        for j in range(m):
            print(room[i][j], end=' ')

        print() 
    print() 



for t in range(T):
    dust_move()

    air_clean() 


answer = 0
for i in range(n):
    for j in range(m):
        answer += room[i][j]

answer += 2
print(answer)





