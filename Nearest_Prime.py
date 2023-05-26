t=int(input())
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
for i in range(t):
    n=int(input())
    if is_prime(n)==1:
        print(n)
        continue
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
    if o-p==q-o:
        print(p)
    elif o-p>q-o:
        print(q)
    else:
        print(p)
