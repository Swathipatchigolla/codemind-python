l=list(map(str,input().split()))
c=0
s='aeiouAEIOU'
for i in l:
    j=0
    k=len(i)-1
    if i[j] in s and i[k] not in s:
        c+=1
print(c)