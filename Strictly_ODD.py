n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]%2!=0 and i%2!=0:
        c+=1
s=n//2
if c==s:
    print(True)
else:
    print(False)