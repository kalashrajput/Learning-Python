#WAP to find whether a number is prime or not.
n=int(input("Enter a number : "));
i=1;
count=0;
while(i<=n):
    if(n%i==0):
        count+=1
    i+=1
if(count==2):
    print("It is a prime number");
else:
    print("No, it is not a prime number");
