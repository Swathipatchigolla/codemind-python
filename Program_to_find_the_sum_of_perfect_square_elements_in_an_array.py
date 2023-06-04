n=int(input())
l=list(map(int,input().split()))
import math
s=0
for i in l:
    if math.sqrt(i).is_integer():
        s+=i
print(s)