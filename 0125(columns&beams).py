def check(answer):
    for x,y,a in answer:
        #기둥인 경우
        if a == 0:
            if y == 0 or (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer:
                continue
            else:
                return False
        elif a == 1:
            if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue
            else:
                return False
    return True



def solution(n, build_frame):
    result = []
    for i in range(len(build_frame)):
        x,y,a,b = build_frame[i]
        if b == 1:
            result.append((x,y,a))
            if not check(result):
                result.remove((x,y,a))
        else:
            result.remove((x,y,a))
            if not check(result):
                result.append((x,y,a))
    answer = map(list, result)
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))


