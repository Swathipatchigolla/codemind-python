l=list(map(str,input().split()))
r=[]
for i in range(len(l)-1,-1,-1):
    r.append(l[i][::-1])
for i in r:
    print(i,end=' ')