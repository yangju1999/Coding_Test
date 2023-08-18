def binary_search(data, m, start, end):
    if start > end:
        return end   
    mid = (start + end) // 2
    
    total = 0
    for d in data:
        if d > mid:
            total += (d-mid)

    if total == m: 
        return mid
     
    elif total < m: 
        return binary_search(data,m, start, mid -1)
    
    else:
        return binary_search(data,m, mid+1, end)
    


n, m = map(int, input().split())
data = list(map(int, input().split()))

max_length = max(data)
result = binary_search(data, m, 0, max_length)

print(result)




    
