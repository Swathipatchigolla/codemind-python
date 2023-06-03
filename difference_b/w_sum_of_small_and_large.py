l=list(map(str,input().split()))
a=b=0
for i in l:
    a+=ord(min(i))
    b+=ord(max(i))
print(abs(a-b))