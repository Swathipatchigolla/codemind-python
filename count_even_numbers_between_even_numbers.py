n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        o1=i
        break
for i in range(n):
    if a[i]%2==0:
        o2=i
c=0
for i in range(o1+1,o2):
    if a[i]%2==0:
        c+=1
print(c)