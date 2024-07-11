#String slicing :
str="Hello, World!";
print("Basic slicing -");
print(str[0:5]);
print("Omitting 'start' & 'stop' -");
print(str[:5]);
print(str[7:]);
print("Using negative indices -");
print(str[-6:]);
print(str[:-7]);
print("Using step -");
print(str[::2]);
print("Reverse string -");
print(str[::-1]);
print("Slicing with all parameters -");
print(str[0::2]);