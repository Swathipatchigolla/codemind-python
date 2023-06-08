a=list(map(int,input().split()))
b=list(map(int,input().split()))
al=bo=0
for i in range(3):
    if a[i]>b[i]:
        al+=1
    elif a[i]<b[i]:
        bo+=1
    else:
        pass
print(al,bo,end=' ')