N = int(input())
#리스트 0부터 시작()
answer = [0] * N
answer[0] = 1 #1
answer[1] = 3 #3
for i in range(2,N):
    answer[i] = answer[i-1] + answer[i-2] * 2
print(answer[N-1])