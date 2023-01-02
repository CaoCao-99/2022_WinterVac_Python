s = input()
y, x = s[0], int(s[1])
data = ['a','b','c','d','e','f','g','h']
cnt = 0
for i in range(len(data)):
    if y == data[i]:
        y = i+1
dy = [2,2,-2,-2,1,1,-1,-1]
dx = [1,-1,1,-1,2,-2,2,-2]
for i in range(8):
    if y + dy[i] <1 or y+dy[i]>8 or x+dx[i]<1 or x+dx[i] >8:
        continue
    cnt+=1
print(cnt)