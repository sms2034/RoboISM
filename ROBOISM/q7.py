# Q7.Python program to find the higgest frequency element in the array.

def fun(a):
    
    counts = 0
    b = a[0]
    
    for i in a :
        
        frequency = a.count(i)
        
        if frequency > counts:
            counts = frequency 
            b = i
    print(b)
    
fun([1,2,3,3,5,4,3,2,0,1,4,5,6,7,4,9,0,7,9,8,4,6,5,4,0,4,3,3,8,4,2])
        