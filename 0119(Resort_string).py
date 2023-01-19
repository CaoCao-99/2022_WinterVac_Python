data = input()
answer = list()
num = 0
for i in data:
    if '0' <= i <= '9':
        num += int(i)
    else:
        answer.append(i)
answer.sort()
answer.append(num)
for i in answer:
    print(i, end = '')