a,b = input().split()
a = int(a)
b = int(b)
if(a>b):
    for i in range (0,b+1):
        if(a<b):
            print(a)
        else:
            print(b)
            break
