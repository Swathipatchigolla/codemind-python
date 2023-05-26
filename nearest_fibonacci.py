a=0
b=1
c=a+b
n=int(input())
if n<=0:
    print(0)
elif n==1:
    print(1)
else:
    while n>c:
        a=b
        b=c
        c=a+b
    r=c
    l=c-a
    if n-l<r-n:
        print(l)
    elif n-l>r-n:
        print(r)
    else:
        print(l,r)