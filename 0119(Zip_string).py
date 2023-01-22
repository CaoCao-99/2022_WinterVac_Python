data = input()
length = len(data)//2
once = True
answer = [0] * (length+1)
print(answer)
for i in range(1,length+1):           #구간을 하나씩 늘려가며 설정
    now_data = data[:i]
    once = True
    for j in range(i,len(data),i):  #늘어가는 구간 만큼 반복문 증가
        next_data = data[j: j+i]
        if now_data == next_data:
            if once:
                once=False
        else:
            if once:
                answer[i] += len(now_data)
            else:
                answer[i] += 1 + len(now_data)
            now_data = next_data
            once=True
    if once:
        answer[i] += len(now_data)
    else:
        answer[i] += len(now_data)+1
answer[0] = 1000
print(answer)
print(min(answer))