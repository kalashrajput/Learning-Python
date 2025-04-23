'''
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
'''

#Create a class:
class myclass:
    x=5
#Create an object of the class:
obj=myclass()
print(obj.x) #Prints the value of x

'''
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
'''

class person:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
obj=person("John",36,"Python")
print(obj.name)
print(obj.age)
print(obj.course) 

'''
The __str__() function controls what should be returned when the class object is represented as a string.
If the __str__() function is not set, the string representation of the object is returned:
'''

class person:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"
obj=person("John",36,"Python")
print(obj) #Prints the string representation of the object