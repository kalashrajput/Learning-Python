#WAP to print fibonacci series.
i=int(input("Enter a number - "));
x=0;
y=1;
z=0;
while(z<=i):
    print(z)
    x=y
    y=z
    z=x+y
