n = int(input())
plan = input().split()
result = [1,1]
for p in plan:
    if p == 'R' and result[1]<n:
        result[1] +=1
    elif p == 'L' and result[1]>1:
        result[1] -=1
    elif p == 'U' and result[0]>1:
        result[0] -=1
    elif p == 'D' and result[0]<n:
        result[0] +=1
print(result[0], result[1])