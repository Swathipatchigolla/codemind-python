n=int(input())
l=list(map(int,input().split()))
s=0
j=n-1
import math
for i in l:
    if i==0:
        j-=1
        continue
    else:
        s+=math.pow(2,j)
        j-=1
print(int(s))