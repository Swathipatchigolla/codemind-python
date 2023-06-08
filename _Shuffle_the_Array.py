n=int(input())
l=list(map(int,input().split()))
k=int(input())
r=[]
i=0
j=k
while i<k:
    r.extend([l[i],l[j]])
    i+=1
    j+=1
for i in r:
    print(i,end=' ')