n, m = map(int,input().split())
root_in = [i for i in range(n+1)] #0~n까지 생성

def find(root_in, x):
    if root_in[x] !=x:
        root_in[x] = find(root_in, root_in[x])
    return root_in[x]

def union(root_in, a, b):
    if a > b:
        root_in[a] = b
    else:
        root_in[b] = a

answer = list()
for i in range(m):
    c,a,b = map(int,input().split())
    a_p = find(root_in, a)
    b_p = find(root_in, b)
    if c == 0 and a_p != b_p:
        union(root_in, a_p,b_p)
    if c == 1:
        if a_p == b_p:
            answer.append("YES")
        else:
            answer.append("NO")
for i in answer:
    print(i)

    # 7 8
    # 0 1 3
    # 1 1 7
    # 0 7 6
    # 1 7 1
    # 0 3 7
    # 0 4 2
    # 0 1 1
    # 1 1 1