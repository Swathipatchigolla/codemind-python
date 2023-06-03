l=list(map(str,input().split()))
s1=[]
s2=[]
v='aeiouAEIOU'
for i in l:
    m=''
    s=''
    for j in i:
        if j in v:
            m+=j
        else:
            s+=j
    s=list(s)
    s.sort()
    s=''.join(s)
    s1.append(s)
    s2.append(m)
y=[]
for q in range(len(l)):
    a=0
    x=''
    for p in l[q]:
        if p in s2[q]:
            x+=p
        else:
            x+=s1[q][a]
            a+=1
    y.append(x)
for i in y:
    print(i,end=' ')