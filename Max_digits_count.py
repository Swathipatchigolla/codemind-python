n=int(input())
l=list(map(int,input().split()))
r=[]
def add(x):
    s=0
    while x>0:
        r=x%10
        s+=1
        x//=10
    return s
for i in l:
    r.append(add(i))
m=max(r)
print(r.count(m))