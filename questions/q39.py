import heapq 

t = int(input())

test_cases = []
INF = int(1e9)
for _ in range(t):
    n = int(input())
    test_case = []
    for _ in range(n):
        test_case.append(list(map(int, input().split())))
    test_cases.append(test_case)

dx = [-1, 0, 1, 0 ]
dy = [0, 1, 0, -1]


for test_case in test_cases:
    n = len(test_case)
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = test_case[0][0]  
    q = []
    heapq.heappush(q, (distance[0][0], 0, 0)) 
    while q:
        cost, x, y = heapq.heappop(q)

        if distance[x][y] < cost:
            continue 

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if  distance[nx][ny] > cost + test_case[nx][ny]:
                    distance[nx][ny] = cost + test_case[nx][ny]
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
    print(distance[n-1][n-1])
                
        
    








    