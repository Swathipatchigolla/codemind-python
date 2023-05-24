def is_prime(x):
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
n=int(input())
if is_prime(n)==1:
    print('prime')
else:
    print('not a prime')