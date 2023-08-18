n = int(input())
data = list(map(int, input().split()))


def find_fixed_point(array, start, end):
    if start > end:
        return -1 
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid 
    elif array[mid] > mid:
        return find_fixed_point(array, start, mid-1)    
    else:
        return find_fixed_point(array, mid+1, end)


answer = find_fixed_point(data, 0, n-1)
print(answer) 