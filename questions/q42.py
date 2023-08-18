gate = int(input())
plane = int(input())
max_gate = []

for _ in range(plane):
    max_gate.append(int(input())) 

gate_data = [False for _ in range(gate)]

count = 0
for i in range(plane):
    succeed = False 
    for j in range(max_gate[i]-1, -1, -1):
        if gate_data[j] == False:
            gate_data[j] = True
            succeed = True 
            break 
    if succeed == False:
        break 
    count += 1

    
print(count)

    

