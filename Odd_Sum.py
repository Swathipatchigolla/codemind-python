s=0
n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i%2==1:
        s+=i
print(s)