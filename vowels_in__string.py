s=input()
l='aeiouAEIOU'
r=[]
for i in s:
    if i in l and i not in r:
        r.append(i)
for i in r:
    print(i,end=' ')