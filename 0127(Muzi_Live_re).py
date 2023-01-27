import heapq
def solution(food_times, k):
    answer = -1
    l = len(food_times)
    #만약, k초 이전에 모든 음식을 섭취할 수 있는 경우 
    if k >= sum(food_times):
        return -1
    q = []
    for i in range(l):
        heapq.heappush(q, (food_times[i], i+1))
    #q에 먹기 가장 작은값을 넣어주며 2번째 인덱스에는 해당 음식의 번호를 넣어준다.
    #q에 값이 존재하는 경우 계속하여 반복
    prev = 0
    while q:
        #현재 가장 작은 값을 갖고있는 음식의 개수를 now count에 담기
        now_count = q[0][0]
        #현재 음식을 먹기위해서 
        now_time = (now_count-prev) * l
        if now_time <= k :
            k -= now_time # 음식 제거
            heapq.heappop(q)
            l -= 1 # 음식의 개수도 하나 제거
            prev = now_count
        else:
            q.sort(key = lambda x : x[1])#음식의 번호로 정렬
            return q[k%l][1]
    return answer


    