n=int(input())
nums=list(map(str,input().split()))
c=0
for i in range(n):
    if len(nums[i])%2==0:
        c+=1
print(c)