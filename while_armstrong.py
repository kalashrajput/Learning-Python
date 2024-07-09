#WA to find whether a number is armstrong or not.
n=int(input("Enter a number : "));
i=n;
count = 0;
sum = 0;
while(i>0):
    i=i//10
    count+=1
i=n;
while(i>0):
    sum = sum + (i%10)*count
    i= i//10
if(n==sum):
    print("Yes, it is an armstrong number");
else:
    print("No, it is not an armstrong number");
