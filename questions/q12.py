import copy 


build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5

def check(struct):
    for element in struct:
        x,y,a = element
        if a == 0: #기둥일때 
            if y != 0 and [x,y-1,0] not in struct and [x,y,1] not in struct and [x-1,y,1] not in struct:
                return  False 

        else: # 보 일때
            if [x,y-1,0] not in struct and [x+1,y-1,0] not in struct and ([x-1,y,1] or [x+1,y,1]) not in struct:
                return False 
    return True 


def solution(n, build_frame):
    result = [] 
    for build in build_frame:
        x, y, a, b = build 
        if b == 0:
            result.remove([x,y,a])
            if not check(result):
                result.append([x,y,a])
        
        else:
            result.append([x,y,a])
            if not check(result):
                result.remove([x,y,a])
    result.sort()
    return result


print(solution(n, build_frame)) 
