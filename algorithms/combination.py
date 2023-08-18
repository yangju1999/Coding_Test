from permutation import permutations
array =[1,2,3,4,5,6]
r = 3


#combination을 바로 작성하는 법 
def combinations(array, r):
    result = [] 
    n = len(array)
    visited = [False for _ in range(n)]
    
    def dfs(start, now):
        if len(now) == r:
            result.append(now)
            return now
        for i in range(start, n):
            if visited[i] == False:
               visited[i] = True 
               dfs(i+1, now+[array[i]]) 
               visited[i] = False 
    dfs(0,[])
    
    
    
    return result

#permutation에서 중복을 제거하는 방법으로 구현 
s =set()
for permutation in permutations(array,3):
    permutation = tuple(sorted(permutation)) 
    s.add(permutation)
print(sorted(list(s)))
    
    


