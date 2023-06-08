a,b=0,1
n=int(input())
print(a,b,end=' ')
while n>2:
    c=a+b
    a=b
    b=c
    print(c,end=' ')
    n-=1