array =[1,2,3,4,5,6]
r = 3

def permutations(array, r):
    result = []
    n = len(array)
    visited = [False for _ in range(n)]

    def dfs(now):
        if len(now) == r:
            result.append(now)
            return now 
        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                dfs(now +[array[i]])
                visited[i] = False 

    dfs([])

    return result


