data = list(map(int, input()))

count = 0
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        count += 1 

if count % 2 == 0:
    print(count//2)
else:
    print(count//2 + 1)


