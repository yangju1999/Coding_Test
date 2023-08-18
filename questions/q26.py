import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

answer = 0 

while len(q) > 1:
    min1 = heapq.heappop(q)
    min2 = heapq.heappop(q)
    new = min1 + min2
    answer += new 
    heapq.heappush(q, new)

print(answer) 

