n=int(input())
l=set(map(int,input().split()))
s=0
for i in l:
    if i%2==1:
        s+=i
print(s)