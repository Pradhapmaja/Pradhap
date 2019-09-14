n=int(input())
a=str(n)
c=0
for i in str(n):
    c+=int(i)**len(a)
print(c)
