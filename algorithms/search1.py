n = int(input())
inventory = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

inventory.sort() 

def binary_search(arr, target, start, end):
    if start > end:
        return None 
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
     
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid -1)
    
    else:
        return binary_search(arr, target, mid+1, end)
    
result = []

for i in range(m):
    if binary_search(inventory, request[i], 0, n-1) != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')



