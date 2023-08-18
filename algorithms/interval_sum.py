# dp 방식으로 접근 
n, m = map(int, input().split())

array = list(map(int, input().split()))
query = []

for _ in range(m):
    start, end = map(int, input().split())
    query.append((start, end))

prefix_sum = [0]

sum_value = 0 

for a in array:
    sum_value += a
    prefix_sum.append(sum_value)

for start, end in query:
    print(prefix_sum[end] -prefix_sum[start-1])
    
    