t=int(input())
for i in range(t):
    n=input()
    if n==n[::-1]:
        print(True)
    else:
        print(False)