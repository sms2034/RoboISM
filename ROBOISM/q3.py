# Q3. Write a Python function that accepts three parameters. The first parameter is
# an integer. The second is one of the following mathematical operators: +, -, /, or .
# The third parameter will also be an integer.

def fun(x,t,y):
    if t =='+':
        return x+y
    elif t == '-':
        return x-y
    elif t == '*':
        return x*y
    elif t == '/':
        return x/y

print("Addition",fun(7,'+',9))
print("Subtraction",fun(7,'-',9))
print("Multiplication",fun(7,'*',9))
print("Division",fun(7,'/',9))


