#WAP to find sum of square of digits of given number.
i=int(input("Enter a number : "));
sum=0;
while(i>0):
    sum=sum+i*i%10
    i=i//10
print("The sum of givin digit is : ",sum);
