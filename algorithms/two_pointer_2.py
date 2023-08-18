n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0 for _ in range(n+m)]


i = 0
j = 0
now = 0  

while i<n and j<m:
    if a[i] < b[j]:
        result[now] = a[i]
        i+=1
        now+=1
    else:
        result[now] = b[j]
        j+=1
        now+=1

if i == n:
    while j != m:
        result[now] = b[j]
        now+=1
        j+=1
else:
    while i != n:
        result[now] = a[i]
        now+=1
        i+=1 

print(result)