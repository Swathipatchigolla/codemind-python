n,k=map(int,input().split())
l=list(map(int,input().split()))
def digits(x):
    s=0
    x=abs(x)
    if x==0:
        s+=1
    while x>0:
        s+=1
        x//=10
    return s
c=0
for i in l:
    if digits(i)==k:
        c+=1
print(c)