N,M,K = map(int, input().split())
list = list(map(int, input().split()))
Big = max(list)
second = min(list)
check, c = False,False
for i in list:
    if Big == i and c ==True:
        check = True
        break
    elif Big ==i:
        c=True
    elif i != Big and second < i:
        second = i
if check:
    print(M*Big)
else:
    print( (M / (K+1)) * (K*Big + second) + M % (K+1) * Big)
