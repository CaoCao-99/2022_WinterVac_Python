def rotation(arr):
    return list(zip(*arr[::-1])) #90도 회전

def check(board,n):
    for i in range(n):
        for j in range(n):
            if board[n+i][n+j] != 1:
                return False
    return True


def solution(key, lock):
    m,n = len(key), len(lock)
    board = [[0] * (3*n) for i in range(3*n)]
    for i in range(n):
        for j in range(n):
            board[n+i][n+j] = lock[i][j] 
    r_key = key
    for a in range(4):
        r_key = rotation(r_key)
        for i in range(2*n):
            for j in range(2*n):
                for x in range(m):
                    for y in range(m):
                        board[i+x][j+y] += r_key[x][y]
                if check(board,n):
                    return True
                for x in range(m):
                    for y in range(m):
                        board[i+x][j+y] -= r_key[x][y]
    return False
                        