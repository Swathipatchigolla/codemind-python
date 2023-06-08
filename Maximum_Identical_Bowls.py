n=int(input())
l=list(map(int,input().split()))
s=sum(l)
while True:
    if (s/n).is_integer():
        print(n)
        break
    n-=1