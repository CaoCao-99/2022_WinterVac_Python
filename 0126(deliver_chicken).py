from itertools import combinations
N, M = map(int , input().split())
board = [list(map(int, input().split())) for i in range(N)]
house = []
h_c = 0
c_c = 0
chicken = []
result = 999999999
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i,j))
            h_c += 1
        elif board[i][j] == 2:
            chicken.append((i,j))
            c_c += 1


for chi in combinations(chicken, M):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house: 
        chi_len = 99999999
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)