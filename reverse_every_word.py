l=list(map(str,input().split()))
r=[]
for i in range(len(l)):
    r.append(l[i][::-1])
for i in r:
    print(i,end=' ')