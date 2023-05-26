a=int(input())
b=int(input())
import math
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,int(math.sqrt(x))+1):
        if x%j==0:
            return 0
    else:
        return 1
c=0
for i in range(a,b+1):
   if is_prime(i)==1:
       c+=1
print(c)