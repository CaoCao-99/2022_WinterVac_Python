N, H = map(int, input().split())
data = list(map(int,input().split()))
start = 0
end = 2000000000
while start <= end:
    mid = (start+end)//2
    diff = 0
    for i in data:
        if i > mid:
            diff+= i-mid
    if diff >= H:
        answer = mid
        start = mid + 1
    else:
        end = mid -1
print(answer)             
