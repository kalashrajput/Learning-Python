#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


#Making dictionaries :
dict={
    "name":"kalash",
    "age":"19",
    "course":"bca"}
dict1={"name":"queen",
       "age":"19",
       "course":"bca"}
print(dict)
print(dict1)
#type of data :
print(type(dict))
#from list of tuples :
lot=[("kalash",19),("mahak",18),("anshu",22)]
print(lot)  
#accessing dictionaries elements via keys :
print(dict["age"])
#accessing dictionaries elements using get() method :
print(dict.get("city","not found"))
#addidng or updating elements :
dict["age"]=26          #updating 
dict["city"]="delhi"    #adding
print(dict)
#removing elements using del() :
del dict["age"]
print(dict)
#removing elements using popitem() :
item=dict.popitem()     # Removes and returns the last inserted key-value pair 
print(dict)  
#clearing dictionay :
dict.clear()            #will clear all the items in dictionary 
#deleting dictionary :
del dict                #will delete whole dictionay
#dictionaries methods :
# 1.keys :
keys = dict1.keys()
print(keys)
# 2.values :
val = dict1.values()
print(val)
# 3.items :
items=dict1.items()
print(items)
# 4.update :
dict1.update({"city":"delhi","age":20})
print(dict1)
# 5.copy :
newdict=dict1.copy()
print(newdict)
# 6.setdefault :
value=dict1.setdefault("sem",3)
print(value)
#Iterating Through Dictionaries via Keys :
for key in dict1:
    print(key,end=" ")
#Iterating Through Dictionaries via values :
for value in dict1.values():
    print(value)
#Iterating Through Dictionaries via key-value pairs :
for key,value in dict1.items():
    print(f"{key}:{value}")
#len :
length=len(dict1)
print(length)
#sorted :
sort=sorted(dict1)
print(sort)
#Counting Occurrences :
sentence = "hello world"
counter = {}
for char in sentence:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1
print(counter)