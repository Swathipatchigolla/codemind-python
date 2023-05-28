n=int(input())
l=list(map(int,input().split()))
k=int(input())
p=[]
c=0
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
for i in range(n):
    if is_prime(l[i])==1:
        p.append(l[i])
for i in p:
    if i<=k:
        c+=1
print(c)