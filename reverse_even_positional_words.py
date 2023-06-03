l=list(map(str,input().split()))
r=[]
for i in range(len(l)):
    if i%2==0:
        r.append(l[i][::-1])
    else:
        r.append(l[i])
for i in r:
    print(i,end=' ')