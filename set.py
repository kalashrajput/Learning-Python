#A set is a collection which is unordered, unchangeable*, and unindexed.

#Making a set:
myset = {"apple", "banana", "cherry"}
print(myset)
#Length of a Set :
print(len(myset))
#type() :
print(type(myset))
#Access Items
#Sets are unordered, so you cannot access items using an index or a key.
#But you can loop through the set items using a for loop:
for i in myset:
    print(i)
#Add Items :
myset.add("strawberry")
print(myset)
#Add Multiple Items :
thisset = {"orange","mango","papaya"}
myset.update(thisset)
print(myset)
#Remove Item :
myset.remove("strawberry")
print(myset)
#join sets :
myset1 = {"kiwi", "grapes"}
myset2 = myset.union(myset1)
print(myset2)
#Intersection of two sets :
myset3 = myset.intersection(myset1)
print(myset3)
#Difference of two sets :
myset4 = myset.difference(myset1)
print(myset4)
#clear() :
myset.clear()
print(myset)
#Delete Set :
del myset
print(myset)