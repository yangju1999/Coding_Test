numbers = list(map(int, input())) 

result = numbers[0]
for i in range(1, len(numbers)):
    result = max(result + numbers[i], result*numbers[i])

print(result)    

