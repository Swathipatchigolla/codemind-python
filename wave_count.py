n=int(input())
l=list(map(int,input().split()))
c=i=0
while i<n-2:
    if l[i]<l[i+1] and l[i+1]>l[i+2]:
        c+=1
    elif l[i]>l[i+1] or l[i+1]<l[i+2]:
        c=-1
        break
    i+=2
if i+1==n-1:
    if l[i]<l[i+1]:
        pass
    else:
        c=-1
print(c)