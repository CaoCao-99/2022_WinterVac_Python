n , m = map(int,input().split())
data = list(map(int,input().split()))
board = [0] * (m+1) #0~m까지의 무게에 맞는 볼링공 개수 저장하는 리스트
for i in data:
    board[i] +=1
answer = 0
for i in range(1,m+1):
    answer += board[i] * sum(board[i+1:m+1]) # 곱하기 이용
print(answer)