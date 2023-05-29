n=int(input())
l=list(map(int,input().split()))
f=1
for i in range(n-1):
    if l[i]>=l[i+1]:
        f=0
if f==1:
    print('yes')
else:
    print('no')