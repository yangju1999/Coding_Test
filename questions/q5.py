n, m = map(int, input().split())

data = list(map(int, input().split()))

weight = [0 for _ in range(m+1)]

for d in data:
    weight[d] += 1

result = 0 
for i in range(1, len(weight)-1):
    for j in range(i+1, len(weight)):
        result += weight[i] * weight[j]

print(result) 



