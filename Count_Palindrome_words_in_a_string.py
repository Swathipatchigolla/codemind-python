l1=list(map(str,input().split()))
l2=[]
c=0
def is_pal(x):
    if x==x[::-1]:
        return 1
    else:
        return 0
for i in l1:
    l2.append(i.lower())
for i in l2:
    if is_pal(i)==1:
        c+=1
print(c)