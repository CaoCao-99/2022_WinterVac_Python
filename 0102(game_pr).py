#입력 값 정리
N,M = map(int,input().split())
y, x, s = map(int, input().split())
# y-=1
# x-=1
dy = [1,0,-1,0]#북 동 남 서
dx = [0,-1,0,1]
game = []
cnt = 0
finish =False
for i in range(N):
    game.append(list(map(int, input().split())))
print(game)
while(not finish):
    for i in range(4):
        ns = (s+i+1)%4  #다음 시점
        ny = y+dy[ns]
        nx = x +dx[ns]
        if N > ny >= 0 and M > nx >= 0 and game[ny][nx] == 0:
            game[ny][nx] = -1
            y,x,s = ny,nx,ns
            cnt +=1
            break
        elif i==3: #반대 방향으로 이동
            ny = y + dy[(s+2)%4]
            nx = x + dx[(s+2)%4]
            if ny < 0 or ny >=N or nx <0 or nx >=M or game[ny][nx]==1:
                finish =True
            else:
                y,x=ny,nx

print(cnt)
            