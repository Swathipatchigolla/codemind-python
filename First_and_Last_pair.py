n=int(input())
l=list(map(int,input().split()))
r=[]
i,j=0,n-1
while i<j:
    r.extend([l[i],l[j]])
    i+=1
    j-=1
if n%2==0:
    pass
else:
    r.extend([l[i],0])
for i in r:
    print(i,end=' ')