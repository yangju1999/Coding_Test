n = int(input())

data = list(map(int, input().split()))

b,c = map(int, input().split())

answer = 0

for i in range(n):
    temp = 1

    if data[i] - b > 0:
        if (data[i] - b) % c ==0: 
            temp += (data[i] - b) // c 
        else:
            temp += (data[i] - b) // c + 1
        
    answer += temp 


print(answer)







