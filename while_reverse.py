#WAP to reverse a given number. 
n=int(input("Enter a number : "));
i=n;
rev=0;
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse of",n,"is",rev);
