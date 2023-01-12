N = int(input())
answer = [0] * (N+1)
p=list()

M = 0
for i in range(N):
    p.append(list(map(int,input().split())))
for i in range(N):
    M = max(M, answer[i])
    if i + p[i][0] <= N:
        answer[i+p[i][0]] = max(M+ p[i][1], answer[i+p[i][0]])
print(max(answer))