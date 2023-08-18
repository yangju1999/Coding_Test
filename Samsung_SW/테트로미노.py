n,m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

max_val = max(map(max, data))

answer = 0  

dx = [1,-1,0,0]
dy = [0,0,1,-1]


visited = [[False for _ in range(m)] for _ in range(n)]

def dfs(start, count, total):
    global answer
    global visited
    x, y = start 
    
    if total + max_val*(4-count) <= answer:
        return 

    if count == 4:
        answer = max(answer, total)
        return 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] =True
                dfs((nx,ny), count + 1, total + data[nx][ny])
                visited[nx][ny] = False 

def special_dfs(start, count, total):
    global answer
    global visited

    x, y = start 
    if count == 4:
        answer = max(answer, total)
        return 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                special_dfs((x,y), count + 1, total + data[nx][ny])
                visited[nx][ny] = False 


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        special_dfs((i,j), 1, data[i][j])
        dfs((i, j), 1, data[i][j])
        visited[i][j] = False 


print(answer) 

