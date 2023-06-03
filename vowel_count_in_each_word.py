l=list(map(str,input().split()))
d=[]
a='aeiouAEIOU'
for i in l:
    c=0
    for j in i:
        if j in a:
            c+=1
    d.append(c)
for i in d:
    print(i,end=' ')