l=list(map(str,input().split()))
c=0
s='aeiouAEIOU'
for i in l:
    j=0
    k=len(i)-1
    while j<=len(i)//2-1:
        if i[j] in s and i[k] not in s or i[j] not in s and i[k] in s:
            c+=1
        j+=1
        k-=1
print(c)