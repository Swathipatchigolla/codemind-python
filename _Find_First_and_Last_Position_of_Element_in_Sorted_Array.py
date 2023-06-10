n=int(input())
a=list(map(int,input().split()))
k=int(input())
x=y=-1
for i in range(n):
    if a[i]==k:
        x=i
        break
while a[i]==k:
    y=i
    i+=1
print(x,y)