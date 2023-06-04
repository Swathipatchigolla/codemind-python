n=int(input())
r=2*n-1
for i in range(r//2):
    m=n
    for j in range(i):
        print(m,end=' ')
        m-=1
    for k in range(r-2*i):
        print(n-i,end=' ')
    m=n-i+1
    for l in range(i):
        print(m,end=' ')
        m+=1
    print()
for i in range(r//2,-1,-1):
    m=n
    for j in range(i):
        print(m,end=' ')
        m-=1
    for k in range(r-2*i):
        print(n-i,end=' ')
    m=n-i+1
    for l in range(i):
        print(m,end=' ')
        m+=1
    print()