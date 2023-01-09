N, M = map(int, input().split())
arr = list(map(int,input()).split())
cost = [10001] * (M+1)
cost[0] = 0

for i in range(N):
    for j in range(arr[i], M+1):
        if cost[j - arr[i]] != 10001:
            cost[j] =  min(cost[j], cost[j - arr[i]]+1)

if cost[M] != 10001:
    print(cost[M])
else:
    print(-1)
