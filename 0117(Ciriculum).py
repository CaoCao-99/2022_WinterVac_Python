from collections import deque   
from copy import deepcopy
n = int(input())
board = [[] for i in range(n+1)]
chasu =[0] * (n+1)
cost = [0] * (n+1)
for i in range(1,n+1):
    inp = list(map(int, input().split()))
    cost[i] = inp[0]
    for j in range(1,len(inp)-1):
        board[inp[j]].append(i)
        chasu[i]+=1
answer = deepcopy(cost)
q = deque()
for i in range(1,n+1):
    if chasu[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in board[now]:
        chasu[i] -=1
        answer[i] = max(answer[i], answer[now] + cost[i])
        if chasu[i] == 0:
            q.append(i)
for i in range(1,n+1):
    print(answer[i])
