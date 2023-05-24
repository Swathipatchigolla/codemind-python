n=input()
l=len(n)
n=int(n)
m=n
s=0
i=l
for j in range(l):
    r=n%10
    s+=pow(r,i)
    i-=1
    n//=10
if s==m:
    print('True')
else:
    print('False')