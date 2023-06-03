n=int(input())
m1=[]
m2=[]
r=[]
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(n):
    m2.append(list(map(int,input().split())))
i=0
for i in range(n):
    x=[]
    a=0
    for k in range(n):
        x.append(m1[i][a]+m2[i][a])
        a+=1
    r.append(x)
    i+=1
for i in r:
    for j in i:
        print(j,end=' ')
    print()