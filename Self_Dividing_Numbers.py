a=int(input())
b=int(input())
for i in range(a,b+1):
    f=1
    x=i
    while i>0:
        r=i%10
        i=i//10
        if r==0:
            f=0
            break
        elif x%r!=0:
            f=0
    if f==1:
        print(x,end=' ')