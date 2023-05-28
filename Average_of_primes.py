n=int(input())
l=list(map(int,input().split()))
p=[]
def is_prime(x):
    if x==0 or x==1:
        return 0
    for j in range(2,x//2+1):
        if x%j==0:
            return 0
    else:
        return 1
for i in range(n):
    if is_prime(l[i])==1:
        p.append(l[i])
print(format((sum(p)/len(p)),".2f"))