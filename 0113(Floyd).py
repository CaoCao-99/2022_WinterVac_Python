INF = int(1e9)

n = int(input())
m = int(input())
board = [[INF] * (n+1) for i in range(n+1)]

#자기 자신 위치는 0으로 초기화
for i in range(1, n+1):
    for j in range(1,n+1):
        if i==j:
            board[i][j] = 0

#값 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    board[a][b] = c

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            board[b][c] = min(board[b][c], board[b][a] + board[a][c])

for a in range(1, n+1):
    for b in range(1,n+1):
        if board[a][b] == INF:
            print("NO", end=' ')
        else:
            print(board[a][b], end=' ')
    print()



