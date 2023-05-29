n=int(input())
l=list(map(str,input().split()))
d=[]
r=[]
for i in l:
    d.append(len(i))
m=max(d)
for i in range(n):
    if d[i]==m and l[i] not in r:
        r.append(l[i])
for i in r:
    print(i,end=' ')