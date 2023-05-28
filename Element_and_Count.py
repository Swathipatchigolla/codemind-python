n=int(input())
l=list(map(int,input().split()))
r=[]
r1=[]
for i in l:
    if i not in r1:
        r1.append(i)
        r.extend([i,l.count(i)])
for i in r:
    print(i,end=' ')