N = int(input())
data = list(map(int, input().split()))
answer = [0] * N
answer[0], answer[1] = data[0],max(data[0],data[1])
for i in range(2,N):
    answer[i] = max(answer[i-2] + data[i], answer[i-1])
print(answer[N-1])