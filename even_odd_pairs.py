n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
i=0
while i<len(e) and i<len(o):
    print(e[i],o[i],end=' ')
    i+=1
while i<len(e):
    print(e[i],end=' ')
    i+=1
while i<len(o):
    print(o[i],end=' ')
    i+=1
if n%2==1:
    print(0)