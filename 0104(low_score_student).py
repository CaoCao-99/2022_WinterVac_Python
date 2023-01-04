N= int(input())
data = []
for i in range(N):
    a = input().split()
    data.append((a[0], int(a[1])))
def setting(arr):
    return(arr[1])
answer = sorted(data, key = setting)

for i,j in answer:
    print(i, end=' ')    
        