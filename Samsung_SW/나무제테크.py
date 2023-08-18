N, M, K = map(int, input().split())

# M = 나무의 개수, K 년이 지난 후 살아있는 나무의 개수 
s2d2 = []

ground = [[5 for _ in range(N)] for _ in range(N)]

trees = []

deads = []

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

for _ in range(N):
    s2d2.append(list(map(int, input().split())))

for _ in range(M):
    x, y, age = map(int, input().split())
    trees.append((age, x-1, y-1)) 

trees.sort()

def spring():
    global ground 
    global trees 
    global deads
    live = []
    
    for tree in trees:
        age, x, y = tree

        if ground[x][y] >= age:
            ground[x][y] -= age 
            live.append((age+1, x, y))
        else:
            deads.append((age//2,x,y))

    trees = live 

def summer():
    global ground
    global trees
    global deads 

    for dead in deads:
        value, x, y=dead
        ground[x][y] += value 

    deads = []

def fall():
    global ground 
    global trees
    news = []

    for tree in trees:
        age, x, y = tree
        if age%5 ==0:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    news.append((1, nx,ny))

    trees = news + trees 

def winter():
    global s2d2
    global ground

    for i in range(N):
        for j in range(N):
            ground[i][j] += s2d2[i][j]
    


for _ in range(K):
    if not trees:
        break   
    spring()
    summer()
    fall()
    winter() 
    
print(len(trees))









