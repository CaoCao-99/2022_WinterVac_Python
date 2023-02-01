def check(data_str):
    open_d = 0
    for i in data_str:
        if i == '(':
            open_d += 1
        else:
            open_d -= 1
        if open_d < 0 :
            return False
    return True

def divide(data_str):
    open_d = 0
    for i in range(len(data_str)):
        if data_str[i] == '(':
            open_d +=1
        else:
            open_d -= 1
        if open_d == 0:
            return data_str[:i+1], data_str[i+1:]




def solution(p):
    if len(p) == 0:
        return p
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer+=')'
            else:
                answer+='('
        return answer

    
