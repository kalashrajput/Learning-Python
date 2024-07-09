#WAP to find is givin number is armstrong number is not.
i=int(input("Enter a number : "));
org=i;
sum=0;
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if(sum==org):
    print(org,"is an armstrong number.");
else:
    print(org,"is not an armstrong number.");
