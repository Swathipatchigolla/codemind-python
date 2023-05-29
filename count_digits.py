n=int(input())
l=list(map(int,input().split()))
d=[]
def digits(x):
    s=0
    x=abs(x)
    if x==0:
        s+=1
    while x>0:
        s+=1
        x//=10
    return s
for i in l:
    d.append(digits(i))
for i in d:
    print(i,end=' ')