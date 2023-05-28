s=0
n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if i%2==0:
        s+=a[i]
print(s)