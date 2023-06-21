m,n=map(int,input().split())
l=[]
s=0
for i in range(m):
    r=list(map(int,input().split()))
    l.append(r)
for i in  range(m):
    for j in range(m):
        if i==j or i+j==m-1:
            s+=l[i][j]
print(s)