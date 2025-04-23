'''
Python does not have built-in support for Arrays, but Python Lists can be used instead.
However, to work with arrays in Python you will have to import a library, like the NumPy library.
An array is a special variable, which can hold more than one value at a time.
'''


fruits=["apple", "banana", "cherry"]
# 1
print(fruits[0]) #Prints the first fruit in the array
# 2
print(fruits[1]) #Prints the second fruit in the array
# 3
x = len(fruits) #Returns the number of elements in the array
print(x) 
# 4
for i in fruits:
    print(i) #Prints all the fruits in the array using a for loop
# 5
fruits.append("strarberry") #Adds a new fruit to the array
print(fruits)

#Example of using the array module:
import array as arr
a = arr.array('f', [1, 2, 3, 4, 5]) #Creates an array with the type code 'i' (integer) and the values 1, 2, 3, 4, 5
print(a[0]) #Prints the first element of the array