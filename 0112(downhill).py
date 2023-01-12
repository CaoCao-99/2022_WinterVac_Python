from collections import deque
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))
dy = [0,0,-1,1]
dx = [-1,1,0,0]
dp =[ [-1] * M for i in range(N)]

dp[0][0] = 1

def dfs(y, x):
    if y == 0 and x == 0:
        return 1
    if dp[y][x] == -1:
        dp[y][x]+=1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and board[y][x] < board[ny][nx]:
                dp[y][x] += dfs(ny, nx)
    return dp[y][x]
print(dfs(N-1,M-1)) 
