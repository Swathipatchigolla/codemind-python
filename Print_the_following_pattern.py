n=int(input())
for i in range(1,n+1):
    x=ord('A')
    r=2*i-1
    for j in range(n-i):
        print(' ',end='')
    for k in range(r//2+1):
        print(chr(x),end='')
        x+=1
    x-=1
    for l in range(r//2):
        x-=1
        print(chr(x),end='')
    print()