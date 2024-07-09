#WAP to print factorial of given number.
n=int(input("Enter a number : "));
i=n;
fact=1;
while(i>0):
    fact=fact*i
    i=i-1
print("Factorial of",n,"is",fact);
    
