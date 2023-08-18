n = int(input())
data = []
for _ in range(n):
   name, score =input().split()
   score = int(score)
   data.append((name, score))

result = sorted(data, key = lambda x:x[1])
for i in range(len(result)):
   print(result[i][0], end = ' ')   
