from itertools import combinations
import copy
N, M = map(int,input().split())
board = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for i in range(N):
    board.append(list(map(int, input().split())))
q = []
n = 0 # 벽 개수
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            n+=1
        elif board[i][j] == 0:
            q.append((i,j))
c_b = copy.deepcopy(board)

answer = 0
count = 0


def DFS(y,x, c_b):
    c_b[y][x] = -1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx  <M and c_b[ny][nx] == 0:
            DFS(ny,nx,c_b)
        elif i == 3:
            return
    return

for i in combinations(q,3):
    c_b = copy.deepcopy(board)
    count = 0
    for j in range(3):
        c_b[i[j][0]][i[j][1]] = 1
    for a in range(N):
        for b in range(M):
            if c_b[a][b] == 2:
                DFS(a,b, c_b)
    for a in range(N):
        for b in range(M):
            if c_b[a][b] == 0:
                count+=1
    answer = max(answer, count)

print(answer)