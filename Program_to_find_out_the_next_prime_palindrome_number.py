n=int(input())
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
def is_pal(x):
    if x==x[::-1]:
        return 1
    else:
        return 0
n+=1
while True:
    if is_pal(str(n))==1 and is_prime(n)==1:
        print(n)
        break
    n+=1