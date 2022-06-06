# Q2.Write a function in Python that accepts a credit card number. It should return a
# string where all the characters are hidden with an asterisk except the last four.


def fun(a):

    b= str(a)
    n= len(b)
    c = '*'*(n-4)
    d = b[n-4:]
    e=c+d
    print(e)
# fun("4576567356367307")
# fun("7894327692014608")      
# print()
inp= input("Enter ypur credit card number : ")
fun(inp)
        