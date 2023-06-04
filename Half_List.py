n=int(input())
l=list(map(int,input().split()))
r=[]
r.extend(l[n//2:][::-1])
r.extend(l[:n//2])
for i in r:
    print(i,end=' ')