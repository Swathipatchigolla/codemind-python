n=int(input())
l=list(map(int,input().split()))
c=0
def is_pal(x):
    y=x
    s=0
    while x>0:
        r=x%10
        s=s*10+r
        x//=10
    if y==s:
        return 1
    else:
        return 0
for i in l:
    if is_pal(i)==1:
        c+=1
print(c)