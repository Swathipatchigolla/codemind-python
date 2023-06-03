s=input()
c=0
for i in s:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):
        c+=1
print(c)