n=int(input())
x=ord('A')+n-1
for i in range(n):
    for j in range(n-i):
        print(chr(x),end=' ')
    x-=1
    print()