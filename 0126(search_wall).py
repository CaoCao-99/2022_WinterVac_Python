from itertools import combinations
def solution(n, weak, dist):
    
    for i in range(1, len(dist)+1):
        for comb in combinations(dist, i):#i명씩 묶어 그룹 만들기
            for j in range(i):

                for w in weak:
                    start = w
                    




    answer = -1
    return answer