import heapq
def solution(food_times, k):
    answer = -1
    l = len(food_times)#테이블 한바퀴 도는데 걸리는 시간
    if sum(food_times) * l <= k:
        return -1
    q = []
    for i in range(l):
        heapq.heappush(q, (food_times[i], i+1))
    prev = 0
    while q:
        now = q[0][0]
        now_time = (now - prev) * l
        prev = now
        if now_time <= k:   #음식을 다 먹을 수 있는 경우
            k -= now_time #남아있는 k초 계산
            l -= 1          #남은 음식 제거
            heapq.heappop(q)
        else:
            result = sorted(q,key = lambda x : x[1])
            idx = k % l
            answer = result[idx][1]
            break
    return answer