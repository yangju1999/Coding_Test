from collections import deque

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(str, input())))

rs = None
bs = None
h = None

for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            bs = (i, j)
        elif board[i][j] == 'R':
            rs = (i, j)
        elif board[i][j] == 'O':
            h = (i, j)


dx = [-1,0,1,0]
dy = [0,1,0,-1]


def move(pos, dx, dy):
    count = 0 
    x, y = pos 
    nx = x
    ny = y 
    while board[nx+dx][ny+dy] != '#' and board[nx][ny] != 'O':
        count += 1
        nx += dx 
        ny += dy 
    return ((nx, ny), count) 
    

def solution():
    
    q = deque()
    q.append((rs,bs,0))
    visited = []
    visited.append((rs, bs))

    while q:
        r, b, count = q.popleft()
        
        if count > 10:
            return -1 
        
        if r[0] == h[0] and r[1] == h[1]:
            return count 
        
        for i in range(4):
            now_dx = dx[i]
            now_dy = dy[i]
            nr, count_r = move(r, now_dx, now_dy)
            nb, count_b = move(b, now_dx, now_dy)
            
            if nb[0] == h[0] and nb[1] == h[1]:
                continue 

            if (nr, nb)  in visited:
                continue 

            if nr[0] == nb[0] and nr[1] == nb[1]:
                if count_r > count_b:
                    nr = (nr[0] - now_dx, nr[1] - now_dy)
                else:
                    nb = (nb[0] - now_dx, nb[1] - now_dy)

            visited.append((nr, nb))
            q.append((nr, nb, count + 1))
    return -1 

print(solution())


            

        
        
        
    






        
    





    
    




