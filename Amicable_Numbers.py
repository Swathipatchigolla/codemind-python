a=int(input())
b=int(input())
x,y=0,0
for i in range(1,a//2+1):
    if a%i==0:
        x+=i
for i in range(1,b//2+1):
    if b%i==0:
        y+=i
if x==b and y==a:
    print('Amicable')
else:
    print('Not Amicable')