n=int(input())
l=set(map(int,input().split()))
l=list(sorted(l))
if len(l)>=3:
    print(l[-3])
else:
    print(max(l))