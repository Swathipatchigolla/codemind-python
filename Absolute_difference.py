def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
n=int(input())
l=list(map(int,input().split()))
pr=npr=1
for i in l:
    if is_prime(i)==1:
        pr*=i
    else:
        npr*=i
print(abs(pr-npr))