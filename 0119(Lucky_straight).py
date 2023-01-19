data = list(map(int,input()))
a = sum(data[:len(data)//2])
b = sum(data[len(data)//2 : len(data)+1])
if a == b:
    print("LUCKY")
else:
    print("READY")