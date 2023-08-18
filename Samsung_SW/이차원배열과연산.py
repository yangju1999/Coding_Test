r,c,k = map(int, input().split())

data = []
for _ in range(3):
    data.append(list(map(int, input().split())))


def transpose(data):
    result = [[0 for _ in range(len(data))] for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            result[j][i] = data[i][j] 
    return result 


def r_operation():
    global data 
    
    for index in range(len(data)):
        temp = data[index]
        appear_count = [0] * 101
        for element in temp:
            appear_count[element] += 1
        
        temp_array = []
        for i in range(1, 101):
            if appear_count[i] > 0:
                temp_array.append((appear_count[i], i))
        temp_array.sort() 

        new_array = []
        for i in range(len(temp_array)):
            for j in range(1,-1,-1):
                new_array.append(temp_array[i][j]) 

        data[index] = new_array 
    
    for i in range(len(data)):
        if len(data[i]) > 100:
            data[i] = data[i][:100]

    max_length = 0 
    for i in range(len(data)):
        max_length= max(max_length, len(data[i]))

    for i in range(len(data)):
        diff = max_length - len(data[i])
        if diff >0:
            data[i] += [0] * diff 
        

def c_operation():
    global data
    new_data = transpose(data)

    for index in range(len(new_data)):

        temp = new_data[index]
        appear_count = [0] * 101
        for element in temp:
            appear_count[element] += 1
        
        temp_array = []
        for i in range(1, 101):
            if appear_count[i] > 0:
                temp_array.append((appear_count[i], i))
        temp_array.sort() 

        new_array = []
        for i in range(len(temp_array)):
            for j in range(1, -1, -1):
                new_array.append(temp_array[i][j]) 

        new_data[index] = new_array
     
    for i in range(len(new_data)):
        if len(new_data[i]) > 100:
            new_data[i] = new_data[i][:100]

    max_length = 0 
    for i in range(len(new_data)):
        max_length= max(max_length, len(new_data[i]))

    for i in range(len(new_data)):
        diff = max_length - len(new_data[i])
        if diff >0:
            new_data[i] += [0] * diff 

    data = transpose(new_data)


def operation():
    global data
    number_of_row = len(data)
    number_of_col = len(data[0]) 

    if number_of_col <= number_of_row:
        r_operation()
    else:
        c_operation()


    
def check():
    global data
    global r
    global c 
    global k 
    if len(data) >= r and len(data[0]) >= c:
        if data[r-1][c-1] == k:
            return True 
    else:
        return False 
    

time = 0 
answer = 0 

while time<=100:
    if check():
        break 
    operation()
    time += 1
    

if time >100:
    print(-1)
else:
    print(time)
    
