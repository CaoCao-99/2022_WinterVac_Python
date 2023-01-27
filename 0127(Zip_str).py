input_str = input()
length = len(input_str) //2 + 1
answer = [0] * length
# 1부터 length까지 나눈 것 중에 값이 가장 작은 것을 도출하여 출력한다.(length까지 반복하여 도출)
for i in range(1, length):
    now_data = input_str[:i]
    first = True
    answer[i] += len(now_data)
    for j in range(i, len(input_str), i):
        next_data = input_str[j: j+i]
        if now_data == next_data:
            if first:
                answer[i] += 1
                first = False
        #같지 않은 경우
        else:
            answer[i]+=len(next_data)
            now_data = next_data
            first = True

answer[0] = 9999999
print(answer)
print(min(answer))