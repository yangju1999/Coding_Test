from collections import deque

t = int(input())

answers = []

for i in range(t):

    n = int(input())
    
    last_rating = list(map(int, input().split()))
    
    m = int(input())
    
    changes = []
    for _ in range(m): 
        changes.append(tuple(map(int, input().split())))

    graph = [[] for _ in range(n+1)]

    in_degree = [0 for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            graph[last_rating[i]].append(last_rating[j])
            in_degree[last_rating[j]] += 1

    for change in changes:
        start, end = change
        if end in graph[start]: #last_rating.index(start) < last_rating.index(end):
            graph[start].remove(end)
            graph[end].append(start)
            in_degree[end] -= 1
            in_degree[start] += 1 
        else:
            graph[end].remove(start)
            graph[start].append(end)
            in_degree[start] -= 1
            in_degree[end] += 1 

    q = deque()
    definite = True 
    possible = True
    count_first = 0 
    for i in range(1, n+1):
        if in_degree[i] == 0:
            count_first += 1
            q.append(i)

    if count_first > 1:
        definite = False 
    
    if count_first == 0:
        possible = False

    if definite == False:
        answers.append("?")
        continue
    if possible == False:
        answers.append("IMPOSSIBLE")
        continue

    answer = []

    while q:
        now = q.popleft()
        answer.append(now)

        count_next = 0 
        for naver in graph[now]:
            in_degree[naver] -= 1
            if in_degree[naver] == 0:
                count_next += 1
                q.append(naver)

        if count_next > 1:
            definite = False 
            break 
        if count_next == 0 and len(answer) != n:
            possible = False
            break

    if definite == False:
        answers.append('?')
        continue
    if possible == False:
        answers.append('IMPOSSIBLE')
        continue 

    answers.append(answer)

for answer in answers:
    if answer == 'IMPOSSIBLE':
        print(answer)
    elif answer == '?':
        print(answer)
    else:
        for a in answer:
            print(a, end=' ')
        print() 








        

