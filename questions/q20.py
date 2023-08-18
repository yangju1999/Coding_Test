from itertools import combinations
from copy import deepcopy 

n = int(input())
data = []
for _ in range(n):
    data.append(input().split())

teachers = []
students= []
empty = []

dx =[-1, 0, 1, 0]
dy =[0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i,j))
        elif data[i][j] == 'S':
            students.append((i,j))
        else:
            empty.append((i,j))


def dfs(temp, v, direction=4):
    x, y = v
    if direction == 4:
        for i in range(4):
            now_direction = i 
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < n and new_y >=0 and new_y < n:
                if temp[new_x][new_y] == 'S':
                    return True 
                elif temp[new_x][new_y] == 'X' or temp[new_x][new_y] == 'T':
                    temp[new_x][new_y] = 'T'
                    if dfs(temp, (new_x, new_y), now_direction):
                        return True 
    else:
        new_x = x + dx[direction]
        new_y = y + dy[direction]
        if new_x >= 0 and new_x < n and new_y >=0 and new_y < n:
            if temp[new_x][new_y] == 'S':
                return True 
            if temp[new_x][new_y] == 'X' or temp[new_x][new_y] == 'T':
                temp[new_x][new_y] = 'T'
                if dfs(temp, (new_x, new_y), direction):
                    return True 

    return False


succeed_count = 0

for selected in list(combinations(empty, 3)):
    for s in selected:
        i, j = s
        data[i][j] = 'O'

    succeed = True
    temp = deepcopy(data)
    for teacher in teachers:
        if dfs(temp, teacher, 4): #s 지역 침범할 경우
            succeed = False
            for s in selected:
                i, j = s
                data[i][j] = 'X'
            break

    if succeed:
        succeed_count += 1
        print('YES')
        break  

if succeed_count == 0:
    print('NO')



    

