import heapq
INF = float("inf")
N,M,K,X = map(int,input().split())
data = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    data[a].append(b)
answer = [INF] * (N+1)
answer[X] = 0
q = []
check = False
heapq.heappush(q, X)
while q:
    now_city  = heapq.heappop(q)
    for i in data[now_city]:
        if answer[i] > answer[now_city] + 1:
            answer[i] = answer[now_city] + 1
            heapq.heappush(q, i)
for i in range(len(answer)):
    if answer[i] == K:
        check = True
        print(i)

if not check:
    print(-1)
