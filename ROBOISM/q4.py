# Q4.Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function
# "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

def fun(a):
    b=list(a)
    c=[]
    for i in b:
        j=i*2
        c.append(j)
    d = "".join(c)
    for k in range (len(c)):
        print (c[k], end= "")
inp = input("enter a string: ")
fun(inp)