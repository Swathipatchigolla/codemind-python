l=list(map(str,input().split()))
d=[]
for i in l:
    d.append(len(i))
print(min(d))