n = int(input())
from itertools import combinations
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = int(1e9)

people = [x for x in range(n)]


for team1 in combinations(people, n//2):
    team2 = []
    for p in people:
        if p not in team1:
            team2.append(p)

    score_1 = 0 
    score_2 = 0 

    for i in range(n//2):
        for j in range(i+1, n//2):
            p1 = team1[i]
            p2 = team1[j]
            score_1 += graph[p1][p2] 
            score_1 += graph[p2][p1]

    for i in range(n//2):
        for j in range(i+1, n//2):
            p1 = team2[i]
            p2 = team2[j]
            score_2 += graph[p1][p2] 
            score_2 += graph[p2][p1]


    answer = min(answer, abs(score_1 - score_2))  


print(answer)