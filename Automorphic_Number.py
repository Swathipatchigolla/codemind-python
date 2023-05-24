n=int(input())
s=n*n
l=len(str(n))
x=pow(10,l)
if s%x==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')