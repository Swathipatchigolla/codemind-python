n=int(input())
l=list(map(int,input().split()))
r=[]
x=[]
y=[]
for i in range(n):
    if i%2==0:
        x.append(l[i])
    else:
        y.append(l[i])
i=j=0
while i<len(x):
    for k in range(y[j]):
        r.append(x[i])
    i+=1
    j+=1
for i in r:
    print(i,end=' ')