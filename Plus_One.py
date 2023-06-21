x=int(input())
digits=list(map(int,input().split()))
r=0
for i in digits:
    r=r*10+i
r+=1
l=[]
while r>0:
    n=r%10
    l.append(n)
    r//=10
l.reverse()
for j in l:
    print(j,end=' ')