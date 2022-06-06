# Q6.FInd all the prime numbers in given range.

def fun(x,y):
    for i in range(x,y):
        
        if i>1:
            for k in range (2,i):
               
                if i%k==0:
                    break
            else:
                print(i)
                
fun(3,20)
print()
fun(12,109)
print()
fun(4,77)
