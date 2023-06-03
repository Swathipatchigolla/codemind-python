l=list(map(str,input().split()))
a=b=0
for i in l:
    print(abs(ord(min(i))-ord(max(i))),end=' ')