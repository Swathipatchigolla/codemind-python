n=int(input())
d=n*n
x,y=0,0
while n!=0:
    r=n%10
    x=x*10+r
    n//=10
b=x*x
while b!=0:
    m=b%10
    y=y*10+m
    b//=10
if d==y:
    print('True')
else:
    print('False')