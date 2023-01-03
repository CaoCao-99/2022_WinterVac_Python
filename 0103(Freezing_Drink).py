#input값 정리하기
N,M = map(int, input().split())
gate = []
for i in range(N):
    gate.append(list(map(int, input())))
#dy, dx 설정
dy = [-1,0,1,0]
dx = [0,1,0,-1]
#visit의 여부를 배열을 따로 생성하지 않고 해당 map의 값을 -1로 교체하여 대신
def recursive(y, x):
    gate[y][x] = -1 #방문한 것으로 기록
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < N and 0 <= nx <M and gate[ny][nx] == 0:
            recursive(ny,nx)
        elif i == 3:
            return

cnt = 0
for i in range(N):
    for j in range(M):
        if gate[i][j] == 0:
            cnt+=1
            recursive(i,j)

print(cnt)





