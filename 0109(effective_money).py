N,M = map(int,input().split())
data = []
for i in range(N):
    data.append(int(input()))
answer = [10001] * (M+1) #0 ~ M
answer[0] = 0

for i in range(N):
    for j in range(data[i], M+1):
        if answer[j - data[i]] != 10001:
            answer[j] = min(answer[j], answer[j - data[i]]+1)

if answer[M] == 10001:
    print(-1)
else:
    print(answer[M])
