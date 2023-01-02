N = int(input())
cnt = 0
answer = 0
for i in range(61):
    if '3' in str(i):
        cnt+=1
for i in range(N+1):
    if '3' in str(i):
        answer += 3600
        continue
    for j in range(60):
        if '3' in str(j):
            answer += 60
        else:
            answer += cnt

print(answer)