n,k=map(int,input().split())
l=list(map(int,input().split()))
r=[]
if k==0 or k==n:
    r=l
else:
    r.extend(l[k:])
    r.extend(l[:k])
for i in r:
    print(i,end=' ')