x=0
n=int(input())
l=[]
for i in range(n):
    l.append(input())
for i in l:
    if '+' in i:
        x+=1
    if '-' in i:
        x-=1
print(x)