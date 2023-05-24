a=list(input())
b=list(set(a))
if sorted(a)==sorted(b):
    print('Unique Number')
else:
    print('Not Unique Number')