n = int(input())

ugly = [0] * n 

ugly[0] = 1 


pos_2 = 0
pos_3 = 0
pos_5 = 0 

for i in range(1, n): 

    ugly[i] = min(ugly[pos_2] * 2, ugly[pos_3]*3, ugly[pos_5] *5)
    if ugly[i] == ugly[pos_2] * 2:
        pos_2 += 1
    if ugly[i] == ugly[pos_3] * 3:
        pos_3 += 1
    if ugly[i] == ugly[pos_5] * 5:
        pos_5 += 1

print(ugly[n-1])
print(ugly)
