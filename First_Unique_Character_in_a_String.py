s=input()
c=0
for j in s:
    if s.count(j)==1:
        print(s.index(j))
        c+=1
        break
if c==0:
    print(-1)