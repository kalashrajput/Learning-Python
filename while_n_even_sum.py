#WAP to find sum of first n even numbers.
n=int(input("Enter a number upto you want to print : "));
i=1;
sum=0;
while(i<n):
    if(i%2==0):
        sum=sum+i
    i=i+1
print("Sum of first n even numbers is : ",sum);
