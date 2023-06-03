n,a=map(int,input().split())
m=[]
s=0
for i in range(n):
    m.append(list(map(int,input().split())))
for i in range(n):
    for j in m[i]:
        s+=j
print(s)