n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

available = [[] for _ in range(n)]

for i in range(n):
    if i + data[i][0] - 1 < n:
        available[i + data[i][0] - 1].append(i) # available[i] i번째 날에 가능해지는 상담 list   

dp = [0 for _ in range(n)]



if data[0][0] == 1:
    dp[0] = data[0][1]
else:
    dp[0] = 0
for i in range(1, n):
    result = dp[i-1] 
    for previous in available[i]:
        if previous == 0:
            result = max(result, data[previous][1])
        else: 
            result = max(result, dp[previous-1] + data[previous][1]) 


    dp[i] = result


print(dp[n-1]) 
    








