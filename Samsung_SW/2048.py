from copy import deepcopy

n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))


# 아래, 위, 오른쪽, 왼쪽 
'''
위쪽: j->i가 오름차순
아래쪽: j->i 가 내림차순  
왼쪽: i->j 가 오름차순  
오른쪽: i->j가 내림차순  
'''
def move(data, index):

    # 위쪽 
    if index == 0:
        for j in range(n):
            top = 0 
            for i in range(1, n):
                if data[i][j] >0:
                    temp = data[i][j]
                    data[i][j] = 0 

                    if data[top][j] == 0:
                        data[top][j] = temp
                        
                    elif data[top][j] == temp:
                        data[top][j] = 2*temp
                        top += 1

                    else: 
                        top += 1
                        data[top][j] = temp 
                        
    # 아래쪽 
    elif index == 1:
        for j in range(n):
            top = n-1
            for i in range(n-2, -1, -1):
                if data[i][j] >0:
                    temp = data[i][j]
                    data[i][j] = 0

                    if data[top][j] ==0:
                        data[top][j] = temp 

                    elif data[top][j] == temp:
                        data[top][j] = 2*temp
                        top -= 1
                     
                    else:
                        top -= 1
                        data[top][j] = temp 
                        

    # 왼쪽 
    elif index == 2:
        for i in range(n):
            top = 0 
            for j in range(1,n):
                if data[i][j] > 0:
                    temp = data[i][j]
                    data[i][j] = 0 

                    if data[i][top] == 0:
                        data[i][top] = temp 

                    elif data[i][top] == temp:
                        data[i][top] = 2*temp
                        top += 1

                    else:
                        top += 1
                        data[i][top] = temp 
    # 오른쪽 
    else:
        for i in range(n):
            top = n-1
            for j in range(n-2,-1,-1):
                if data[i][j] > 0:
                    temp = data[i][j] 
                    data[i][j] = 0 

                    if data[i][top] == 0:
                        data[i][top] = temp 

                    elif data[i][top] == temp:
                        data[i][top] = 2*temp
                        top -= 1

                    else:
                        top -= 1
                        data[i][top] = temp 
                                   
    return data
    

def check_max(data):
    result = 0 
    for i in range(n):
        for j in range(n):
            result = max(data[i][j], result) 
    return result 


def dfs(data, count):
    global answer
    if count == 5:
        answer = max(answer, check_max(data))
        return 

    for i in range(4):
        new_data = move(deepcopy(data), i)
        dfs(new_data, count+1)
    

answer = 0 
dfs(board, 0)

print(answer)




