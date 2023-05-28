n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
r=[]
for i in a:
    if i in b and i not in r:
        r.append(i)
for i in r:
    print(i,end=' ')