n=int(input())
a=list(map(int,input().split()))
m=min(a)
i=1
while i<=m:
    f=1
    for j in range(n):
        if a[j]%i!=0:
            f=0
    if f==1:
        g=i
    i+=1
print(g)