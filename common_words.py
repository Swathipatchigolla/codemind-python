s1=list(map(str,input().split()))
s2=list(map(str,input().split()))
s3=[]
for i in s1:
    s3.append(i.upper())
for i in s2:
    if i in s1:
        print(i,end=' ')
    elif i.upper() in s3:
        print(i,end=' ')