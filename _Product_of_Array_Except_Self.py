n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    p=1
    for j in l:
        if i==j:
            pass
        else:
            p*=j
    r.append(p)
for i in r:
    print(i,end=' ')