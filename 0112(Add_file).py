N = int(input())



def recursive(start, end):
    if dp[start][end] != -1:
        return dp[start][end]
    elif start == end:
        return 0    #
    ans = float('inf')#무한대
    s = sum(data[start:end+1])
    for i in range(start, end):
        t = recursive(start,i) + recursive(i+1, end) + s
        if ans > t:
            ans = t
        dp[start][end] = ans
    return ans

for i in range(N):
    M = int(input())
    dp = [[-1] * (M+1) for i in range(M+1)]
    data = list(map(int, input().split()))
    print(recursive(0, M-1))


