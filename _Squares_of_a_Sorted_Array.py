n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
r=[]
for i in a:
    r.append(i*i)
r.sort()
for i in r:
    print(i,end=' ')