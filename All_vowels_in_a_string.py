s=input()
a='aeiou'
b='AEIOU'
f=1
for i in a:
    if i not in s:
        f=0
        break
else:
    f=1
if f==0:
    for i in b:
        if i not in s:
            f=0
            break
    else:
        f=1
if f==1:
    print('True')
else:
    print('False')