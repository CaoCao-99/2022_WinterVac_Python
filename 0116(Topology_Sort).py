from collections import deque

u, v= map(int, input().split())
in_table = [0] * (u+1)  #진입 차수를 나타내는 리스트(0~u)
data = [[] for i in range(u+1)]
for i in range(v):
    a,b = map(int,input().split())
    data[a].append(b)
    in_table[b] += 1    #진입 차수 1씩 늘려주기

q = deque()
def put (in_table):
    for i in range(1,u+1):
        if in_table[i] == 0:
            q.append(i)

put(in_table)
while q:
    now = q.popleft()
    print(now,end = '->')
    for i in data[now]:
        in_table[i] -=1
        if in_table[i] == 0:
            q.append(i)
        
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# 1->2->5->3->6->4->7->