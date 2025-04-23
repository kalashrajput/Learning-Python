'''
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''
import os

f = open("pyq.txt","r") 
print(f.read()) # read the file
f.close() # close the file

f= open("pyq.txt","a") # open the file in append mode
f.write("\nThis is a new line") # write to the file
f = open("pyq.txt","r")
f.close() # close the file

f=open("pyq.txt","w") # open the file in write mode
f.write("AHAHAH I am overwriting") # write to the file
f= open("pyq.txt","r")
f.close()

if os.path.exists("ptr.txt"): # check if the file exists
    os.remove("ptr.txt") # remove the file
else:
    print("The file does not exist") # print if the file does not exist

if os.path.exists("pyq.txt"): # check if the file exists
    os.remove("pyq.txt") # remove the file
else:
    print("The file does not exist") # print if the file does not exist