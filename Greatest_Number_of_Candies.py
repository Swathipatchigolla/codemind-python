n=int(input())
l=list(map(int,input().split()))
c=int(input())
m=max(l)
r=[]
for i in l:
    if i+c >= m:
        r.append('True')
    else:
        r.append('False')
for i in r:
    print(i,end=' ')