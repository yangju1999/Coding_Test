def solution(food_times, k):

    total = sum(food_times)
    if total <= k:
        return -1 

    n = len(food_times)
    index = 0
    while k != 0:
        if food_times[index] != 0:
            food_times[index] -= 1
            k -= 1
            

        index  = (index + 1) % n

    return index + 1

print(solution([8,6,4], 15))


