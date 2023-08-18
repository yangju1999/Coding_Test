t = int(input()) #test 횟수 
test_cases= []

for _ in range(t):
    n, m = map(int, input().split())
    test_case = [[-1 for j in range(m)] for i in range(n)]  
    temp = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            test_case[i][j] = temp[i*m + j]
    test_cases.append(test_case)

for test_case in test_cases:    
    n=len(test_case)
    m = len(test_case[0])

    table = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        table[i][0] = test_case[i][0]
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                table[i][j] = max(table[i][j-1], table[i+1][j-1]) + test_case[i][j] 
            elif i == n-1:
                table[i][j] = max(table[i-1][j-1], table[i][j-1]) + test_case[i][j] 
            else:
                table[i][j] = max(table[i-1][j-1], table[i][j-1], table[i+1][j-1]) + test_case[i][j] 
    

    print(max([row[m-1] for row in table]))

