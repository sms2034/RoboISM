#Q1. Create a function in Python that accepts two parameters. The first will be a list
# of numbers. The second parameter will be a string that can be one of the following
# values: asc, desc, and none.



def fun(numberlist, cond):

    if cond == "asc":
        numberlist.sort()
        print("Element in Ascending Order is : ", numberlist)
    elif cond== "desc":
        numberlist.sort(reverse=True)
        print("Element in descending Order is : ", numberlist )
    else:
        print("none")
    
series=input("whether in asc or desc:\n")    
fun([2,5,0,8,6,3,4,7],series)