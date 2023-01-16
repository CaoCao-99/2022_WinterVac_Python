u, v = map(int, input().split())
parent =[i for i in range(u+1)] #0~u까지의 리스트 생성 및 본인으로 부모 노드 초기화

# find_root 함수(재귀적으로 부모 노드를 탐색)
def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]
# union_root 함수(두개 중 더 큰 부모의 노드의 부모 노드 값을 다시 설정)
def union_root(a_p,b_p):
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

#간선의 정보 담기(sort)
board = list()
for i in range(v):
    a,b,c = map(int,input().split())
    board.append((c,a,b))

#코스트를 기준으로 정렬 진행
board.sort()

answer = 0
for i in range(v):
    a_p = find_root(parent, board[i][1])
    b_p = find_root(parent, board[i][2])
    if a_p != b_p:
        union_root(a_p, b_p)
        answer += board[i][0]

print(answer)

# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25


#정답 : 159