n=int(input())
m=o=n
def is_pal(x):
    y=x
    a=0
    while x>0:
        r=x%10
        a=a*10+r
        x//=10
    if a==y:
        return 1
    else:
        return 0
while True:
    if is_pal(n-1)==1:
        p=n-1
        break
    n-=1
while True:
    if is_pal(m+1)==1:
        q=m+1
        break
    m+=1
if o-p==q-o:
    print(p,q)
elif o-p>q-o:
    print(q)
else:
    print(p)