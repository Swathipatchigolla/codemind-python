s=input()
l='aeiou'
r=[]
for i in l:
    if i not in s and i not in r:
        r.append(i)
r.sort()
if len(r)==0:
    print(0)
else:
    for i in r:
        print(i,end=' ')