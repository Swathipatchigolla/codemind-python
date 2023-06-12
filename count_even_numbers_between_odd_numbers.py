n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]%2==1:
        o1=i
        break
for i in range(n):
    if a[i]%2==1:
        o2=i
try:
    for i in range(o1+1,o2):
        if a[i]%2==0:
            c+=1
    print(c)
except:
    print(0)