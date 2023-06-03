n,a=map(int,input().split())
m=[]
e=o=0
for i in range(n):
    m.append(list(map(int,input().split())))
for i in range(n):
    for j in m[i]:
        if i%2==0:
            e+=j
        else:
            o+=j
print(e,o)