from collections import deque
N, K = map(int,input().split())
data = []
virus_q = []
cnt = 0
check_cnt = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
q = []
for i in range(N):
    data.append(list(map(int,input().split())))
S,Y,X = map(int,input().split())
for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            virus_q.append((data[i][j],i,j))

virus_q.sort()
q = deque(virus_q)
time = 0
while q:
    if time == S:
        print(data[Y-1][X-1])
        exit()
    for z in range(len(q)):
        now_num, now_y, now_x = q.popleft()
        for i in range(4):
            ny = now_y+dy[i]
            nx = now_x+dx[i]
            if 0<=nx<N and 0<=ny<N and data[ny][nx] == 0:
                data[ny][nx] = now_num
                q.append((now_num,ny,nx))
    time+=1


print(data[Y-1][X-1])


