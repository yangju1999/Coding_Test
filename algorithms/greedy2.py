n, m = map(int, input().split())
data = [[0 for j in range(m)] for i in range(n)]
min_list = []

for i in range(n):
    data[i] = list(map(int ,input().split()))
    min_list.append(min(data[i]))

print(max(min_list))


