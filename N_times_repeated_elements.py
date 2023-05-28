n=int(input())
l=list(map(int,input().split()))
k=int(input())
r=[]
c=0
for i in l:
    if k==l.count(i) and i not in r:
        r.append(i)
        c+=1
if c==0:
    print(-1)
else:
    for i in r:
        print(i,end=' ')