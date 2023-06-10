t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(1,n+1):
        if i not in a and i not in b:
            print('NO')
            break
    else:
        print("YES")