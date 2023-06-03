s=input()
k=input()
for i in s:
    if i==k:
        print('True')
        print(s.index(i))
        break
else:
    print('False')