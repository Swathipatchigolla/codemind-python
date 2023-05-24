n=int(input())
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
if is_prime(n)==1:
    while n>0:
        r=n%10
        if is_prime(r)==0:
            print('Not Mega Prime')
            break
        n//=10
    else:
        print('Mega Prime')
else:
    print('Not Mega Prime')