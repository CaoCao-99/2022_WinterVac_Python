import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
board = [[] for i in range(n+1)]
visit = [False] * (n+1)
table =[INF] * (n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    board[a].append((b,c))


def get_small_node():
    min_val = INF
    min_idx = 0
    for i in range(1,n+1):
        if visit[i] == False and table[i] < min_val:
            min_idx = i
            min_val = table[i]
    return min_idx
#start 지점에 대한 초기화 부분
table[start] = 0
visit[start] = True
for i in board[start]:
    table[i[0]] = i[1]
#그 외의 table 값 변경 부분
for _ in range(n-1):
    now = get_small_node()
    visit[now] = True
    for j in board[now]:
        if table[j[0]] > table[now] + j[1]:
            table[j[0]] = table[now]+j[1]
for i in range(1,n+1):
    if table[i] == INF:
        print("NO")
    else:
        print(table[i])



# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2