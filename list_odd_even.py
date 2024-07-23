#WAP to find odd and even numbers in a list :
l=[]
size=int(input("How many elements do you want ? "))
for i in range(size):
    val=int(input("Enter value - "))
    l.append(val)
odd=0
even=0
for i in range(size):
    if l[i]%2==0:
        even+=1
    else:
        odd+=1
print(f"No. of Odd values are {odd} and Even values are {even}")