def solution(n, stages):
    data = [0 for _ in range(n+2)]

    for stage in stages:
        data[stage] += 1

    fail_rate = []

    for i in range(1, n+1):
        if sum(data[i:]) != 0: 
            fail_rate.append(((data[i] /  sum(data[i:])), i))
        else:
            fail_rate.append((0, i))
    fail_rate.sort(key = lambda x: (-x[0], x[1])) 
    
    return list(map(lambda x:x[1], fail_rate))


    
