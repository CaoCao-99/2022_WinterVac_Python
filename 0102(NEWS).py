N = int(input())
data = input().split()
locate = [1,1]
x,y = 1,1
dx = [0, 0, -1, 1]
dy = [1, -1 ,0 ,0]
info = ['U', 'D' , 'L', 'R']
for i in data:
    for j in range(len(info)):
        if i == info[j]:
            nx = x + dx[j]
            ny = y + dy[j]
            break
    if nx > N or nx < 1 or ny <1 or ny <N:
        continue
    x,y = nx , ny
    
print(x, y)         
