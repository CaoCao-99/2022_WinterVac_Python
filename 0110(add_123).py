def recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recursive(n-2) + recursive(n-1) + recursive(n-3)

N = int(input())

for i in range(N):
    a = int(input())
    print(recursive(a))
