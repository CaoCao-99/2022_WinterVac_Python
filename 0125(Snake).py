N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for i in range(K)]
L = int(input())
move = [list(input().split()) for i in range(L)]
directions = [(0,1), (1,0), (0,-1), (-1,0)]
board = [[0] * (N+1) for i in range(N+1)]
time = 0
snake = []
for i in range(K):
    board[apple[i][0]][apple[i][1]] = 2 # 사과 집어 넣기
#초기화
board[1][1] = 1
now = (1,1)
snake.append((1,1))
#tail = (1,1)
snake.append
d = 0 #우측으로 이동
prev_dir  = directions[d]

for _ in range(int(move[0][0])):
    time += 1
    next = (now[0] + directions[d][0], now[1] + directions[d][1])
    if 0 < next[0] <= N and 0 < next[1] <= N and board[next[0]][next[1]] !=1:
        if board[next[0]][next[1]] != 2:
            a,b = snake.pop(0)
            board[a][b] = 0       
        now = next
        board[next[0]][next[1]] = 1
        snake.append((next[0], next[1]))
    else:
        print(time)
        exit() 
move.append((10000, 'R'))


#이동하기
for i in range(L):
    if move[i][1] == 'L':
        d = (d - 1) % 4
        dir = directions[d]
    else:
        d = (d + 1) % 4
        dir = directions[d]
    for j in range(int(move[i+1][0]) - int(move[i][0])):
        time+=1
        next = (now[0] + dir[0], now[1] + dir[1])
        if 0 < next[0] <= N and 0 < next[1] <= N and board[next[0]][next[1]] !=1:
            if board[next[0]][next[1]] != 2:
                a,b = snake.pop(0)
                board[a][b] = 0       
            now = next
            board[next[0]][next[1]] = 1
            snake.append((next[0], next[1]))
        else:
            print(time)
            exit() 
print(time)