from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())

data = []
virus_list= []

lab = [[-1 for _ in range(n)] for _ in range(n)] #-1은 빈칸을 의미함 

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 2: 
            virus_list.append((i,j))
            lab[i][j] = '*' #비활성 버이러스 
        elif data[i][j] == 1:
            lab[i][j] = '-' #벽 

answer = int(1e9)

# 0: 활성 바이러스 
# *: 비활성 바이러스 
# - : 벽 
#-1: 빈칸 

def spread(new_lab):
    temp = deepcopy(new_lab) 
    for x in range(n):
        for y in range(n):
            if temp[x][y] == 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<= nx< n and 0<= ny< n:
                        if temp[nx][ny] != '-':
                            new_lab[nx][ny] = 0 
    if temp == new_lab:
        return False
    else:
        return True
                    
def check(new_lab):
    for i in range(n):
        for j in range(n):
            if new_lab[i][j] == -1:
                return False 
    return True 


if check(lab):
    answer = 0 
    
else:
    for virus in combinations(virus_list, m):
        new_lab = deepcopy(lab)
        for x,y in virus:
            new_lab[x][y] = 0 #0은 활성 바이러스를 의미함 
        
        time = 0 
        changed = True

        while changed:
            time += 1
            if time >= answer:
                break 
            changed = spread(new_lab)
            if check(new_lab):
                answer = min(answer, time)
                break 


if answer == int(1e9):
    answer = -1 

print(answer)

        



