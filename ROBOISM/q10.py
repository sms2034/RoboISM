# Q10. Python program to swap two numbers using xor.

def fun(x1,x2):
  
    x1^= x2;
    x2^= x1;
    x1^= x2;
    print(x1)
    print(x2)
    
fun(23,46)
print()
fun(56,12)
