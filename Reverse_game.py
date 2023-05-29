n=int(input())
l=list(map(int,input().split()))
r=[]
def rev(x):
    y=x
    s=0
    while x>0:
        r=x%10
        s=s*10+r
        x//=10
    return s
for i in l:
    r.append(rev(i))
for i in r:
    print(i,end=' ')