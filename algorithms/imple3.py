position_string=input()
colum = int(ord(position_string[0])) - int(ord('a')) + 1
row = int(position_string[1])
count = 0 
dx =[-2, -2, 2, 2, 1, 1, -1, -1]
dy =[-1, 1, -1, 1, 2, -2, 2, -2]

for i in range(len(dx)):
    if 0 < colum + dx[i] < 9 and 0 < row + dy[i] < 9:
        count += 1
print(count) 
