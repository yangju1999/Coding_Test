#BFS ! 
from collections import deque

dx =[-1, 0, 1, 0]
dy =[0, 1, 0, -1]


def next_pos(pos, board):
    n = len(board)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1] 
    available_next = []
    for i in range(4):
        new_pos1_x = pos1_x + dx[i]
        new_pos1_y = pos1_y + dy[i]
        new_pos2_x = pos2_x + dx[i]
        new_pos2_y = pos2_y + dy[i]
        if board[new_pos1_x][new_pos1_y] == 0 and board[new_pos2_x][new_pos2_y] == 0:
            available_next.append(((new_pos1_x, new_pos1_y),(new_pos2_x, new_pos2_y)))
    if pos1_x == pos2_x: # 가로 
        for i in [-1,1]:
            if board[pos1_x+i][pos1_y] ==0 and board[pos2_x+i][pos2_y] == 0:
                available_next.append(((pos1_x,pos1_y),(pos1_x+i, pos1_y)))
                available_next.append(((pos2_x,pos2_y),(pos2_x+i, pos2_y)))
                
    elif pos1_y == pos2_y: # 세로
        for i in [-1,1]:
            if board[pos1_x][pos1_y+i] ==0 and board[pos2_x][pos2_y+i] == 0:
                available_next.append(((pos1_x,pos1_y),(pos1_x, pos1_y+i)))
                available_next.append(((pos2_x,pos2_y),(pos2_x, pos2_y+i)))
    return available_next


def solution(board):
    n = len(board)
    new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    q = deque() 
    start =((1,1),(1,2))
    q.append((start, 0))
    visited = []
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost 
        for new_pos in next_pos(pos, new_board):
            if new_pos not in visited:
                visited.append(new_pos) 
                q.append((new_pos, cost + 1))
    return 0 

board = [[0,0,0,1,1], [0,0,0,1,0],[0,1,0,1,1], [1,1,0,0,1],[0,0,0,0,0]]
print(solution(board))