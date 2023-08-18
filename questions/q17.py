import heapq 

n,k = map(int, input().split())

data = []
for _ in range(n):
	data.append(list(map(int, input().split())))

s, x, y = map(int, input().split())


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


first_q = [] 
for i in range(n):
	for j in range(n):
		if data[i][j] > 0:
			heapq.heappush(first_q, (data[i][j], i, j))
        
second_q = []

for i in range(s):
    if i % 2 == 0:
        q = first_q
    else: 
        q = second_q
    while q:
        priority, x_pos, y_pos = heapq.heappop(q)
        for j in range(4):
            new_x = x_pos + dx[j]
            new_y = y_pos + dy[j]
            if new_x >= 0 and new_x<n and new_y >=0 and new_y < n and data[new_x][new_y] == 0:
                data[new_x][new_y] = priority
                if i % 2 == 0: 
                    heapq.heappush(second_q, (priority, new_x, new_y)) 
                else:
                    heapq.heappush(first_q, (priority, new_x, new_y))

    
print(data[x-1][y-1])