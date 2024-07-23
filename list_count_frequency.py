#WAP to find frequency of a number.
l=[]
size=int(input("How many elements do you want ? "))
for i in range(size):
    val=int(input("Enter value - "))
    l.append(val)
key=int(input("Enter the number - "))
count=0
for i in range(size):
    if l[i]==key:
        count+=1
print(f"Frequene of {key} is {count}")