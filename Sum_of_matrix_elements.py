m=int(input())
n=int(input())
l=[]
s=0
for i in range(m):
    l.append(list(map(int,input().split())))
for i in l:
    for j in i:
        s+=j
print(s)