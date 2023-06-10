n=int(input())
nums=list(map(int,input().split()))
i=int(input())
ind=list(map(int,input().split()))
t=[]
for i in range(n):
    t.insert(ind[i],nums[i])
for i in t:
    print(i,end=' ')