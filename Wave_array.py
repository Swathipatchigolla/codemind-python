n=int(input())
l=list(map(int,input().split()))
i=0
f=1
if l[i]<l[i+1]:
    x='+'
else:
    x='-'
while i<n-2:
    if x=='+':
        if l[i]>l[i+1] or l[i+1]<l[i+2]:
            f=0
            break
    elif x=='-':
        if l[i]<l[i+1] or l[i+1]>l[i+2]:
            f=0
            break
    i+=2
if i+1==n-1:
    if x=='+':
        if l[i]>l[i+1]:
            f=0
    elif x=='-':
        if l[i]<l[i+1]:
            f=0
if f==0:
    print('no')
else:
    print('yes')