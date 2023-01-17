def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]

def union_root(root, a,b):
    if a > b: 
        root[a] = b
    else:
        root[b] = a

n, m = map(int,input().split())
root = [i for i in range(n+1)] # 0 ~ n
board = []
for i in range(m):
    a,b,c = map(int,input().split())
    board.append((c,a,b)) #sort를 위해 cost 값을 0번째 원소로 지정
board.sort()
answer = 0 # 최종 정답
big = 0
for i in range(m):
    a = find_root(root, board[i][1])
    b = find_root(root, board[i][2])
    if a != b:
        union_root(root,a,b)
        answer += board[i][0]
        if big < board[i][0]:
            big = board[i][0]
print(answer - big)