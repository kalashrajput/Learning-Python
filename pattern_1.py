'''
123*
12***              
1*****
*******  
'''
n=int(input("Enter no.of rows you want to print - "))
i=1
for i in range(1,n):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()

print("-----------")

'''
*
**
***
****
'''
n=int(input("Enter no.of rows you want to print - "))
for i in range(1,n):
    print("*"*i,end="")
    print()

print("-----------")

'''
123*
12**
1***
****
'''
n=int(input("Enter no.of rows you want to print - "))
for i in range(1,n):
    print(" "*(n-i),end="")
    print("*"*i,end="")
    print()

print("-----------")

'''
* * *
*   *
* * *
'''
n=int(input("Enter no.of rows you want to print - "))
for i in range(1,n+1):
    if((i==1) or (i==n)):
        print("*"*n)
    else:
       print("*"+" "*(n-2)+"*")
       '''
       print("*",end="")
       print("",end="")
       print("*")
       '''
print()

print("-----------")

'''
123*
12***              
1*****
*******
1*****
12***
123*
'''
n=int(input("Enter no.of rows you want to print (should be an odd number) - "))
middle=(n//2)+1
for i in range(1,middle-1):
    print(" "*(middle-i),end="")
    print("*"*(2*i-1),end="")
    print(" "*(middle-i))
for i in range(middle+1,0,-1):
    print(" "*(middle-i),end="")
    print("*"*(2*i-1),end="")
    print(" "*(middle-i))
