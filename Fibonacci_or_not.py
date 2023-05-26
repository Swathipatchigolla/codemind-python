n=int(input())
a=0
b=1
c=a+b
if n==0 or n==1:
    print(True)
else:
    while n>=c:
        if n==c:
            print(True)
            break
        else:
            a=b
            b=c
            c=a+b
    else:
        print(False)