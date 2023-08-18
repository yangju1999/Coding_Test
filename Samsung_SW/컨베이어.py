n, k = map(int, input().split())


data = list(map(int, input().split()))


count = 0 # 내구도가 0인 칸의 개수 
step = 0

start_pos = 0 
#end_pos = start_pos + n -1

robots = [0 for _ in range(2*n)]


def prev(start_pos):
    if start_pos == 0:
        return 2*n-1 
    else:
        return start_pos -1 
    
def next(pos):
    if pos == 2*n-1:
        return 0 
    else:
        return pos + 1
        

def robot_step():
    global count 
    global start_pos
    global robots 
    start_pos = prev(start_pos)
    end_pos = (start_pos + n -1) % (2*n)
    if robots[end_pos] == 1:
        robots[end_pos] = 0

    i = prev(end_pos)  

    while i != start_pos: 
        if robots[i] == 1:
            next_pos = next(i)
            if robots[next_pos] != 1 and data[next_pos] >= 1:
                if next_pos == end_pos:
                    robots[i] = 0 
                    data[next_pos] -= 1
                    if data[next_pos] == 0:
                        count += 1
                    
                    
                else:
                    robots[next_pos] = 1
                    robots[i] = 0
                    data[next_pos] -= 1
                    if data[next_pos] == 0:
                        count += 1
        i = prev(i)

    if data[start_pos] != 0:
        robots[start_pos] = 1
        data[start_pos] -= 1
        if data[start_pos] == 0:
            count += 1
    
while count < k:
    step += 1
    robot_step()

print(step)

