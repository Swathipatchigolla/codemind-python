s=input()
c=0
for i in s:
    if ord(i)>=ord('a') and ord(i)<=ord('z'):
        c+=1
print(c)