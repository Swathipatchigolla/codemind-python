e=[]
o=[]
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i%2==1:
        e.append(i)
    else:
        o.append(i)
for i in e:
    print(i,end=' ')
for i in o:
    print(i,end=' ')