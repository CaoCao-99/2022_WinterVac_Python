data = list(map(int,input()))
now = data[0]
board = [0,0]

for i in range(len(data)):
    if now != data[i]:
        now = data[i]
        board[now] +=1
if board[0] > board[1]:
    print(board[1])
else:
    print(board[0])
