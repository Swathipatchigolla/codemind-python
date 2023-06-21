m,n=map(int,input().split())
l=[]
s=0
for i in range(m):
    r=list(map(int,input().split()))
    l.append(r)
for i in  range(m):
    for j in range(m):
        if i==0 or i==m-1 or j==0 or j==m-1:
            s+=l[i][j]
print(s)