l=list(input())
s=[]
m=''
x=''
for i in l:
    if i.isalnum():
        s.append(i)
    else:
        m+=i
    s.sort()
k=0
for i in l:
    if i in m:
        x+=i
    else:
        x+=s[k]
        k+=1
print(x)