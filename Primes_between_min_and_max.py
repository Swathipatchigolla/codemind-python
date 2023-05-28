n=int(input())
l=list(map(int,input().split()))
p=[]
x=l.index(min(l))
y=l.index(max(l))
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
m=min(x,y)
q=max(x,y)
for i in range(m,q+1):
    if is_prime(l[i])==1:
        p.append(l[i])
print(len(p))