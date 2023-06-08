s=input()
p=''
for i in s:
    if int(i)%2==1:
        p+=str(int(i)*int(i))
print(p)