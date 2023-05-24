n=int(input())
l=list(map(int,input().split()))
o,e=0,0
for i in range(n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
print(abs(e-o))