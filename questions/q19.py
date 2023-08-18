from itertools import permutations

INF = int(1e9)
n = int(input())
data =list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())
operations = [0] * plus
operations += [1] * minus
operations += [2] * multiple
operations += [3] * divide


max_answer = -INF
min_answer = INF 

for operation in permutations(operations, n-1):
    result = data[0]
    for i in range(1, n):
        if operation[i-1] == 0:
            result += data[i]
        elif operation[i-1] == 1:
            result -= data[i]
        elif operation[i-1] == 2:
            result *= data[i]
        else:
            if result < 0:
                result = -result 
                result = result // data[i]
                result = -result 
            else:
                result = result// data[i] 
    max_answer = max(max_answer, result)
    min_answer = min(min_answer, result)

print(max_answer)
print(min_answer)

        
        





 