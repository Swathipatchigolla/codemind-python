n=int(input())
p=[]
h=[]
c=0
for i in range(n):
    p.append(int(input()))
for i in range(n):
    h.append(int(input()))
for i in p:
    for j in h:
        if i<=j:
            h.remove(j)
            c+=1
            break
print(n-c)