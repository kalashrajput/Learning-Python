#WAP to accept marks of 5 subjects and find total marks and percentage assuming full marks as 100
#in each subject.
sub1=int(input("Enter marks of subject 1 - "));
sub2=int(input("Enter marks of subject 2 - "));
sub3=int(input("Enter marks of subject 3 - "));
sub4=int(input("Enter marks of subject 4 - "));
sub5=int(input("Enter marks of subject 5 - "));
totalmarks=sub1+sub2+sub3+sub4+sub5;
percentage=(totalmarks/500)*100;
print("------ REPORT CARD ------");
print("Marks in sub1 - ",sub1);
print("Marks in sub2 - ",sub2);
print("Marks in sub3 - ",sub3);
print("Marks in sub4 - ",sub4);
print("Marks in sub5 - ",sub5);
print("Total marks - ",totalmarks);
print("Percentage - ",percentage,"%");
