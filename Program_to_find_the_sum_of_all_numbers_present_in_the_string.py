s=input()
p=0
for i in s:
    if i.isdigit():
        p+=int(i)
print(p)