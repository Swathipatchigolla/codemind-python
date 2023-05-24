a=int(input())
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
b=0
if is_prime(a)==1:
    while a>0:
        r=a%10
        b=b*10+r
        a//=10
    if is_prime(b)==1:
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')