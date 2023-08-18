def rotate_matrix_90_degree(a):
    n = len(a) 
    m = len(a[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result  


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, 2*lock_length):
            if new_lock[i][j] != 1:
                return False 
    return True 
    

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0 for _ in range(3*n)] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    rotate_key = key 
    for _ in range(4):
        rotate_key =  rotate_matrix_90_degree(rotate_key)
        for x_pos in range(2*n):
            for y_pos in range(2*n):
                for i in range(m):
                    for j in range(m):              
                        new_lock[x_pos+i][y_pos+j] += rotate_key[i][j] 
                if check(new_lock): 
                    return True 
                for i in range(m):
                    for j in range(m): 
                        new_lock[x_pos+i][y_pos+j] -= rotate_key[i][j] 
                        
    return False 


key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

print(solution(key, lock))