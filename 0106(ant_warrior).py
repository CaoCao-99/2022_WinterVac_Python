a = [0] * 100
N = int(input())
data =list(map(int, input().split()))
a[0] = data[0]
a[1] = data[1]
for i in range(2, N, 1):
    a[i] = max(a[i-2]+data[i], a[i-1])
print(a[i])