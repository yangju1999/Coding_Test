n, m = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

d = [10001] * (m+1) 
d[0] = 0

for i in range(1, m+1):
    for coin in coin_list:
        if i>=coin:
            d[i] =  min(d[i], d[i-coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])


    



