from collections import deque

n = int(input())
k = int(input())
apple = [[0 for _ in range(n)] for _ in range(n)]
direction = {}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for _ in range(k):
    x_pos, y_pos = map(int, input().split())
    apple[x_pos-1][y_pos-1] = 1

l = int(input())

for _ in range(l):   #x = 숫자  c = 문자  L이면 왼쪽 D이면 오른쪽 
    x, c =input().split()
    x = int(x) 
    direction[x] = c 

def change_direction(c, now_direction):
    if c == 'L':
        new_direction = (now_direction - 1) % 4 
    else:
        new_direction = (now_direction + 1) % 4 
    return new_direction

total_time = 0 
snake_body = deque()
snake_head = [0,0]
snake_direction = 0 # 초기 방향 dx[0], dy[0] 
while True:

    if total_time in direction.keys():
        snake_direction = change_direction(direction[total_time], snake_direction) 

    new_x = snake_head[0] + dx[snake_direction]
    new_y = snake_head[1] + dy[snake_direction]
    snake_body.append((snake_head[0], snake_head[1]))
    
    if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in snake_body:
        if apple[new_x][new_y] == 1:
            apple[new_x][new_y] = 0 
        else:
            snake_body.popleft()
        
        snake_head[0] = new_x
        snake_head[1] = new_y
        total_time += 1 

    else:
        total_time += 1
        break 

print(total_time)






