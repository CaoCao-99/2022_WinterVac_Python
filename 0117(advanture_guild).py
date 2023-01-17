n = int(input())
cost = [0] * (n+1)
#input값 받기
c = list(map(int, input().split()))
for i in c:
    cost[i] +=1
#
remain = 0
answer = 0
for i in range(1,n+1):
    answer += ((cost[i] + remain)//i)
    remain = cost[i] % i
print(answer)
