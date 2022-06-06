# Q8.Python program to calculate sum of integers in string.
def fun(a):
    b= list(a)
    c=['0','1','2','3','4','5','6','7','8','9']
    add = 0
    for i in b:
        if i in c:
            add+= int(i)
    print(add)
inp= input("Enter a string: ")
# fun("1N73LL1G3NC3 15 4B1L17Y 70 4D4P7 70 CH4NG3")
fun(inp)
