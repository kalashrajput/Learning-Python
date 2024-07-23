#wAP to find sumof list elements :
l=[]
size=int(input("How many elements you want to enter ? "))
for i in range(size):
    val=int(input("Enter value - "))
    l.append(val)
sum=0
for i in range(size):
    sum = sum + l[i]
print(f"Sum of elements are {sum}")