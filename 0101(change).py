import time

n = int(input())
change = [500, 100, 50, 10]
count = 0

s_t = time.time()
for i in change:
    count+=n//i
    n%=i
print(count)
e_t = time.time()
print(e_t - s_t)


#테스트 입력값: 12353156211
# 12353156211
# 24706315
# 3.2480318546295166

