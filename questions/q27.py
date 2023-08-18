from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

left_index=bisect_left(data, x)
right_index = bisect_right(data, x)

result = right_index - left_index

if result == 0:
    print(-1) 
else:
    print(result)

