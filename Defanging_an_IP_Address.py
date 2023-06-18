s=input()
l=''
for i in s:
    if i=='.':
        l+='[.]'
    else:
        l+=i
print(l)