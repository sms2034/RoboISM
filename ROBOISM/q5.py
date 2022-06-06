# Q5. Write a program in Python for finding that one number from an array of 100 numbers(with values ranging from 1 to 99) which is duplicate.
def fun(a):
    b=[]
    for j in a:
        if j not in b:
            b.append(j)
        else:
            print(j,end='')
fun([1,2,3,4,5,6,8,12,9,0,12,23,24,25,26,67])
