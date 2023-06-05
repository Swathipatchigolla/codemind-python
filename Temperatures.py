n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    c=0
    for j in range(i+1,n):
        if a[i]<a[j]:
            c+=1
            break
        else:
            c+=1
    if a[i]>=a[j]:
        c=0
    b.append(c)
for i in b:
    print(i,end=' ')