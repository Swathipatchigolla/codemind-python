t=int(input())
for j in range(t):
    n=int(input())
    l=set(map(int,input().split()))
    a=[i for i in range(1,n+1)]
    r=list(l.union(a)-l.intersection(a))
    for k in r:
        print(k)