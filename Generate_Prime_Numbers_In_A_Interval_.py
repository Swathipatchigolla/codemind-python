a=int(input())
b=int(input())
l=[]
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
for i in range(a,b+1):
   if is_prime(i)==1:
       l.append(i)
for i in l:
    print(i)