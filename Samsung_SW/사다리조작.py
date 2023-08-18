n, m, h = map(int, input().split())

graph = [[False for _ in range(n+1)] for _ in range(h+1)]

edges = []

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = True 

def check():
    global graph 
    for start in range(1, n+1):
        now_h = 1
        now_col = start 
        while now_h <= h:
            if graph[now_h][now_col]:
                now_h += 1
                now_col += 1
            elif graph[now_h][now_col-1]:
                now_h += 1
                now_col -= 1
            else:
                now_h += 1

        if start != now_col:
            return False
    return True

answer = 4

def dfs(count, index):
    global answer 
    if count > 3:
        return 
    if check():
        answer = min(answer, count)
        return 
    if count ==3:
        return 
    for i in range(index, h+1):
        for j in range(1, n):
            if graph[i][j] == False and graph[i][j+1] == False and graph[i][j-1]== False:
                graph[i][j] = True 
                dfs(count+1, i)
                graph[i][j] = False

dfs(0, 1)
if answer == 4:
    print(-1)
else:
    print(answer)


    
