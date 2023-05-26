a,b=map(int,input().split())
m=max(a,b)
mn=min(a,b)
for i in range(1,m+1):
    if (m*i)%mn==0:
        print(m*i)
        break