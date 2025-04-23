'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
'''

# Example 1:
x = lambda a: a - 10
print(x(20))

# Example 2:
x = lambda a,b: a*b
print(x(10,8))

# Example 3:
def func(n):
    global y 
    y = lambda a: a + n
func(20)
print(y(5))