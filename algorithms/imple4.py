n, m = map(int, input().split())
row_pos, col_pos, direction = map(int, input().split())
sea_map = []
for _ in range(n):
    sea_map.append(list(map(int, input().split())))

direction_dict = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[row_pos][col_pos] = 1
result = 1 

while True:
    rotate_count = 0 
    for _ in range(4):
        direction = (direction-1)%4
        d_row, d_col = direction_dict[direction] 
        new_row = row_pos +d_row 
        new_col = col_pos +d_col 
        if 0<=new_row<n and 0<=new_col<m and visited[new_row][new_col] == 0 and sea_map[new_row][new_col] != 1:
            row_pos = new_row 
            col_pos = new_col 
            visited[row_pos][col_pos] = 1
            result += 1
            break 
        else:
            rotate_count +=1

    if  rotate_count != 4:
        continue

    else:
        d_row, d_col = direction_dict[(direction+2)%4]
        new_row = row_pos + d_row 
        new_col = col_pos + d_col 
        if sea_map[new_row][new_col] == 1:
            break 
        else:
            row_pos = new_row 
            col_pos = new_col 
            continue

print(result) 






