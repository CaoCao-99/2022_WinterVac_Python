import heapq


def solution(food_times, k):
    answer = -1
    l = len(food_times)#테이블 한바퀴 도는데 걸리는 시간
    q = []
    for i in range(l):
        heapq.heappush(q, (food_times[i], i+1))
    print(q)
    time = 0
    while q:
        time = q[0][0] * l  
        if time <= k:   #음식을 다 먹을 수 있는 경우
            k -= time #남아있는 k초 계산
            l -= 1          #남은 음식 제거
            heapq.heappop(q)
        else:
            q = q.sort(key = lambda x : x[1])
            idx = l % k
            answer = q[idx][1]
    return answer