data = [0]*1000001 # 결과값(횟수)을 담아 둘 리스트 생성
N = int(input())

for i in range(2, N+1):
    data[i] = data[i-1] + 1 #1을 빼는 경우
    if i % 3 == 0:
        data[i] = min(data[i], data[i//3] + 1) # 3으로 나누는 경우와, 1을 뺀 경우를 비교하여 최소 횟수 반환
    if i %  2 == 0:
        data[i] = min(data[i], data[i//2] + 1) # 2로 나눈 경우와 앞서 나온 최소 횟수와 비교하여 작은 값 반환
print(data[N])

