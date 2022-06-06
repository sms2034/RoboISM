# Q9.. Python Program to sort characters of a string in ascending order


def fun(a):
    b= list(a)
    b.sort()
    c="".join(b)
    print(c)
inp = input("Enter a string: ")
fun(inp)