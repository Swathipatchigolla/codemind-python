n=int(input())
l=list(map(int,input().split()))
x=0
for i in range(n//2):
    x+=l[i]
y=sum(l)-x
print(abs(x-y))