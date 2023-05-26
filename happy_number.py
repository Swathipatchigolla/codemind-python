n=int(input())
while True:
    s=0
    while n>0:
        r=n%10
        s+=r*r
        n//=10
    if s%10==s:
        break
    else:
        n=s
if s==1 or s==7:
    print(True)
else:
    print(False)