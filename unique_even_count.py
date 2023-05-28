n=int(input())
l=set(map(int,input().split()))
s=0
for i in l:
    if i%2==0:
        s+=1
print(s)