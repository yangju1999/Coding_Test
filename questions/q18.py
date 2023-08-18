def check_correct(u):
    stack = 0  
    for i in range(len(u)):
        if u[i] == '(':
            stack += 1
        else:
            if stack > 0:
                stack -= 1
            else:
                return False 
    return True 
    
def balanced_index(p):
    count = 0 
    for i in range(len(p)):
        now = p[i]
        if now == '(':
            count += 1
        elif now == ')':
            count -= 1
        if count == 0:
            return i  


def solution(p):
    answer = ''
    if p == '':
        return answer
    
    if check_correct(p):
        return p 
    
    i = balanced_index(p)

    u = p[:i+1]
    v = p[i+1:]
    if check_correct(u):
        return u + solution(v)
    else:
        temp = '('+solution(v)+')'
        u = u[1:-1]

        for ele in u:
            if ele == '(':
                temp += ')'
            else:
                temp += '('
        return temp 


print(solution('()))((()'))