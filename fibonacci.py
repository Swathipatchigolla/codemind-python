n=int(input())
a,b=0,1
print(a,b,end=' ')
n-=2
while n>0:
    c=a+b
    a=b
    b=c
    print(c,end=' ')
    n-=1