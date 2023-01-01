N, M = map(int, input().split())
ans = list()
for i in range(N):
    data = list(map(int, input().split()))
    ans.append(min(data))
print(max(ans))