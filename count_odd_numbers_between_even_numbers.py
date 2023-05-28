n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        e1=i
        break
for i in range(n):
    if a[i]%2==0:
        e2=i
c=0
for i in range(e1,e2+1):
    if a[i]%2==1:
        c+=1
print(c)