import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
n,m,start = map(int,input().split())
#들어오는 값 입력 받기(board 리스트 생성 2차원)
board = [[] * (n+1) for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    board[a].append((b,c))
table = [INF] * (n+1)
table[start] = 0
q = []
heapq.heappush(q,(0,start))
print(board)
while q:
    dist, now  = heapq.heappop(q)
    #이미 거쳐간 경우 제외
    if table[now] < dist:
        continue
    #현재의 위치에서 갈 수 있는 공간 탐색
    for i in board[now]:
        if table[i[0]] > dist + i[1]:
            table[i[0]] = dist + i[1]
            heapq.heappush(q,(table[i[0]], i[0]))

cnt = 0
table[0] = 0
for i in range(1,n+1):
    if table[i] == INF:
        cnt +=1
        table[i] = -1
print(n - cnt -1, end=' ')
print(max(table))