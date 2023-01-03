#input
from collections import deque
N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int, input())))
#dy,dx
dy = [-1,0,1,0]
dx = [0,-1,0,1]

#BFS
queue = deque()
queue.append((0,0))
while queue:
    y,x = queue.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        elif board[ny][nx] == 1:
            board[ny][nx] = board[y][x] + 1 # 1추가
            queue.append((ny,nx))
print(board[N-1][M-1])
