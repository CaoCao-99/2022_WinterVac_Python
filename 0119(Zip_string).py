data = input()
length = len(data)//2
once = True
answer = [0] * (len(data)//2 +1)
print(answer)
for i in range(1,length):           #구간을 하나씩 늘려가며 설정
    for j in range(0,len(data),i):  #늘어가는 구간 만큼 반복문 증가
        print(j)
        now_data = data[j:j+i]
        answer[i] += i
        once = True
        next_data = data[j+i: j+2*i]
        if now_data == next_data:
            if once:
                answer[i]+=1
                once = False
            else:
                continue

answer[0] = 1000
answer[length] = 1000
print(answer)
print(min(answer))