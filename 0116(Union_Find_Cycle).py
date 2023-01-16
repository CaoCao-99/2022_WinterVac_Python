u, v = map(int, input().split())
parent =[i for i in range(u+1)] #0~u까지의 리스트 생성 및 본인으로 부모 노드 초기화
Cycle = False
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

for i in range(v):
    a,b = map(int,input().split())
    a_p = find_root(parent, a)
    b_p = find_root(parent, b)
    if (a_p == b_p):
        print("사이클이 존재합니다.")
        exit()
    else:
        union_root(a_p,b_p)
print("사이클이 존재하지 않습니다.")
        


