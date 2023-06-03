l1=list(map(str,input().split()))
l2=list(map(str,input().split()))
l3=[]
l4=[]
c=0
for i in l1:
    l3.append(i.lower())
for i in l2:
    l4.append(i.lower())
for i in l3:
    if i in l4:
        c+=1
print(c)