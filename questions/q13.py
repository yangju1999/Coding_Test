from itertools import combinations 
n,m =map(int, input().split())

city = []
chicken = []
house = []

for _ in range(n):
    city.append(list(map(int, input().split()))) 

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        if city[i][j] == 1:
            house.append((i,j))

def max_city_chicken_distance(chicken, house):
    result = 0

    for h in house:
        temp = 2*n 
        for c in chicken:
            temp = min(temp, abs(h[0] - c[0]) + abs(h[1]-c[1]))
        result += temp 
    return result

answer = 2*n*len(house)
for alive_chicken in list(combinations(chicken, m)):
    answer = min(answer, max_city_chicken_distance(alive_chicken, house))

print(answer)     


