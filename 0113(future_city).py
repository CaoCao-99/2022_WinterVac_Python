import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int,input().split())
board = [[INF] * (n+1) for i in range(n+1)]

#동일 위치 0으로 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            board[i][j] = 0

#값 입력받기(양방향 설정)
for i in range(m):
    a,b = map(int,input().split())
    board[a][b] = 1
    board[b][a] = 1
x, t =  map(int,input().split())   


for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

if board[1][t] == INF or board[t][x] == INF:
    print(-1)
else:
    print(board[1][t]+board[t][x])