import heapq
N, K = map(int,input().split())
data = []
virus_q = []
cnt = 0
check_cnt = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
check = [[True] * (N) for i in range(N)]
print(check)
q = []
for i in range(N):
    data.append(list(map(int,input().split())))
S,Y,X = map(int,input().split())
for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            heapq.heappush(virus_q, (data[i][j], i,j))
            check[i][j] = False
            cnt += 1

q = virus_q
time = 0
while q:
    check_cnt+=1
    now_num, now_y, now_x = q.pop(0)
    for i in range(4):
        ny = now_y+dy[i]
        nx = now_x+dx[i]
        if 0<=nx<N and 0<=ny<N and data[ny][nx] == 0:
            data[ny][nx] = now_num
            q.append((now_num,ny,nx))
    if check_cnt == cnt:
        time+=1
        check_cnt = 0
        cnt = 0
        for i in range(N):
            for j in range(N):
                if data[i][j] != 0 and check[i][j] == True:
                    cnt += 1
                    check[i][j] = False
    if time == S:
        print(data[Y-1][X-1])
        exit()

print(data[Y-1][X-1])


