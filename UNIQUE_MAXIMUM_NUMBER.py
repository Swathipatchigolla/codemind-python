n=int(input())
l=list(map(int,input().split()))
s=set(l)
r=[]
c=0
for i in s:
    if l.count(i)==1:
        r.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(max(r))