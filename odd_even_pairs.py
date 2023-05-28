n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==1:
        o.append(i)
    else:
        e.append(i)
i=0
while i<len(e) and i<len(o):
    print(o[i],e[i],end=' ')
    i+=1
while i<len(o):
    print(o[i],end=' ')
    i+=1
while i<len(e):
    print(e[i],end=' ')
    i+=1
if n%2==1:
    print(0)