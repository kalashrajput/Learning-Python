#WAP to find max in three numbers.
a=int(input("Enter 1st number - "));
b=int(input("Enter 2nd number - "));
c=int(input("Enter 3rd number - "));
if((a>b) and (a>c)):
    print("a is bigger");
elif((b>a) and (b>c)):
    print("b is bigger");
else:
    print("c is bigger");
