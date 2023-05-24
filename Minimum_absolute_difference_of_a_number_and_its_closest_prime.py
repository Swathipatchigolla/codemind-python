def is_prime(x):
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
n=int(input())
m=o=n
while True:
    if is_prime(n-1)==1:
        p=n-1
        break
    n-=1
while True:
    if is_prime(m+1)==1:
        q=m+1
        break
    m+=1
if is_prime(o)==1:
    print('0')
elif o-p==q-o:
    print(o-p)
elif o-p>q-o:
    print(q-o)
else:
    print(o-p)