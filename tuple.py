#Making a tuple :
t=(1,2,3,4,5,6)
print(t)
#accessing a tuple :
print(t[5])
print(t[-4])
#slicing :
print(t[2:5])
print(t[-5:-2])
print(t[-2:-5:-1])
#creating string to tuple :
s="laddoo"
t1=tuple(s)
print(t1)
#creating list to tuple :
l=[1,2,3,4]
t2=tuple(l)
print(t2)
#concatenation :
print(t1+t2)
#repetition :
print(t2*7)
#membership testing :
if 2 in t:
    print("2 is present")
else:
    print("2 is not present")
#length :
print(len(t2))
#count :
print(t2.count(3))
#max :
print(max(t))
#min :
print(min(t1))
#index :
print(t1.index('d'))
#adding values to tuple by using list :
l1=list(t)
l1.append(7)
t3=tuple(l1)
print(t3)