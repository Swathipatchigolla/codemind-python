n1=int(input())
n2=int(input())
x=y=n1+n2
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
while True:
    if is_prime(x+1)==1:
        p=x+1
        break
    x+=1
print(p-y)