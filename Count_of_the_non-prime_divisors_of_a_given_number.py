n=int(input())
l=[]
c=0
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if is_prime(i)==0:
        c+=1
print(c)