n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    c=0
    for j in l:
        if i!=j and j<i:
            c+=1
    r.append(c)
for i in r:
    print(i,end=' ')