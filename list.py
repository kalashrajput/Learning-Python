#Making a list :
l=[1,2,3.5,"hello",True,[5,6,7]]
l1=[1,2,3,1,5,1,8,6]
print(l)
#Accessing :
print(l[3])
print(l[5][2])
#updating values :
l[2]=5
print(l)
#slicing :
li=l[2:5:1]
print(li)
#printing list using for loop :
for i in l:
    print(i)
#deleting a value :
del l[2]
print(l)
l.pop(2)
print(l)
#inserting value :
l.append(100) #will add the value to the end of the list.
print(l)
l.insert(2,10) #will add the value to the endex which you have given.
print(l)
#list comprehension :
n=[m for m in range(1,25,3)]
print(n)
b="Kaleshu"
c=[d for d in b]
print(c)
#count :
e=l1.count(1)
print(e)
#max :
print(max(l1))
#min :
print(min(l1))
#reverse :
h=l1.reverse
print(h)
#sort : 
g=l.sort
print(g)
#index :
print(l1.index(5))
#concatination :
print(l+l1)
#converting a string in list :
u="Pohu Bhai"
U=list(u)
print(U)
j=u.split()
print(j)