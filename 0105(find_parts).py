N = int(input())
d_N = list(map(int, input().split()))
M = int(input())
d_M = list(map(int,input().split()))

def binary_search(data, start, end):
    while start <= end:
        mid = (start + end) // 2
        if data == d_N[mid]:
            return "yes"
        elif data < d_N[mid]:
            end = mid-1
        else:
            start = mid+1 
    return "no"

d_N.sort()
print(d_N)
for i in d_M:
    print(binary_search(i,0,N-1),end = ' ')

