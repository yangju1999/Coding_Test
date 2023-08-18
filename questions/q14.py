from itertools import permutations

def solution(n, weak, dist):

    number_weak = len(weak)
    temp = []  
    for w in weak:
        temp.append(w + n)
    weak = weak + temp 

    answer = len(dist) + 1

    for start in  range(number_weak):
        for friends in list(permutations(dist, len(dist))):
            count = 1 
            position = weak[start] + friends[count-1]
            for index in range(start, start + number_weak):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break 
                    position = weak[index] + friends[count-1]  
            answer = min(answer, count)
    if answer > len(dist):
        return -1 
    
    return answer 



