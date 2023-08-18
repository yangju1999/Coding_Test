# 구간 합이 M 인 연속된 구간 개수 구하기 
n, m = map(int, input().split())
array = list(map(int, input().split()))

count = 0 
interval_sum = array[0] 
start = 0
end = 0

while True:
    if end >= n or start >=n: 
        break 

    if interval_sum == m:
        count += 1
        interval_sum -= array[start]
        start += 1
        end += 1
        if end ==n:
            break 
        interval_sum += array[end]

    elif interval_sum  > m:
        interval_sum -= array[start]
        start += 1

    else:
        end += 1
        if end ==n:
            break 
        interval_sum += array[end]

print(count) 

    


