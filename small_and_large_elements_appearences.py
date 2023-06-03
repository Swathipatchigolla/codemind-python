s=input()
l=''
for i in s:
    if i!=' ':
        l+=i
print(min(l),l.count(min(l)),max(l),l.count(max(l)))