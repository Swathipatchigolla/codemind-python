n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
i=j=0
while i<n:
    c.append(a[i]+b[j])
    i+=1
    j+=1
for i in c:
    print(i,end=' ')