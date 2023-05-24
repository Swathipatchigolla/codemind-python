n=int(input())
c=0
for i in range(1,n//2+1):
    for j in range(i,n//2+1):
        if i*j==n:
            print(i,j)
            c+=1
            break
if c==0:
    print('-1')