#기존의 다익스트라에서 최단 값을 갖는 노드에 들인 시간을 줄여서 시간복잡도를 줄이자.(우선순위 큐(힙) 사용)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
board = [[] for i in range(n+1)]
visit = [False] * (n+1)
table =[INF] * (n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    board[a].append((b,c))



#heap 사용(우선순위 큐)

q= []
heapq.heappush(q, (0,start))
table[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if table[now] < dist: #이미 방문한 경우
        continue
    for i in board[now]:
        if table[i[0]] > dist + i[1]:
            table[i[0]] = dist+i[1]
            heapq.heappush(q,(table[i[0]], i[0]))

for i in range(1,n+1):
    if table[i] == INF:
        print("NO")
    else:
        print(table[i])



# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
