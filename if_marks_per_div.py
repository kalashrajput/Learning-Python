#WAP  to calculate total marks in 5 subjects with percentage and division.
sub1=int(input("Enter marks of sub1: "));
sub2=int(input("Enter marks of sub2: "));
sub3=int(input("Enter marks of sub3: "));
sub4=int(input("Enter marks of sub4: "));
sub5=int(input("Enter marks of sub5: "));
totalmarks=sub1+sub2+sub3+sub4+sub5;
percent=int(totalmarks/500*100);
print("----------- REPORT CARD -----------");
print("Total marks - ",totalmarks);
print("Percentage - ",percent,"%");
if(percent>=80):
    print("Congratulation! you got 'A' grade.");
elif(percent>=60):
    print("Congratulation! you got 'B' grade.");
elif(percent>=40):
    print("Keep it up! you got 'C' grade");
else:
    print("Need to work hard! you got 'D' grade");
