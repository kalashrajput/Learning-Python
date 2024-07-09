#WAP to find the product of given number.
n=int(input("Enter a number : "));
i=n;
prod=1;
while(i>0):
    prod=prod*(i%10)
    i=i//10
print("Product of",n,"is",prod);
