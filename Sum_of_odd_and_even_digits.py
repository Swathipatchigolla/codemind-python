n=int(input())
l=list(map(int,input().split()))
e=o=0
for i in range(n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if e-o==0:
    print('YES')
else:
    print('NO')