data = []

for _ in range(4):
    data.append(list(map(int, input())))

#N극은 0, S극은 1
#2번, 6번 톱니가 맞닿는 톱니임 

k = int(input()) 

rotate_list = [] 

for _ in range(k):
    index, direction = map(int, input().split())
    rotate_list.append((index-1, direction)) # 1이면 시계방향 -1이면 반시계 방향


def clockwise(data):
    result = []
    result.append(data[-1])
    for i in range(len(data)-1):
        result.append(data[i])
    return result 
    
def counter_clockwise(data):
    result = []
    for i in range(1, len(data)):

        result.append(data[i])
    result.append(data[0])
    return result

def check_point(data):
    result = 0
    if data[0][0] == 1:
        result += 1
    if data[1][0] == 1:
        result+=2
    if data[2][0] == 1:
        result+=4
    if data[3][0] == 1:
        result+=8
    return result

for rotate in rotate_list:
    index, direction = rotate

    changed = [0 for _ in range(4)]
    changed[index] = direction 

    now_index = index 
    now_direction = direction 

    while now_index < 3:
        if data[now_index][2] == data[now_index+1][6]:
            break 
        else:
            now_direction = now_direction * -1 
            changed[now_index+1] = now_direction  

        now_index += 1

    now_index = index 
    now_direction = direction

    while now_index > 0:
        if data[now_index][6] == data[now_index-1][2]:
            break 
        else:
            now_direction = now_direction* -1 
            changed[now_index-1] = now_direction  

        now_index -= 1
    
    for i in range(4):
        dir = changed[i]
        if dir == 1:
            data[i] = clockwise(data[i])

        elif dir == -1:
            data[i] = counter_clockwise(data[i])


print(check_point(data))