# Q11.Write a Python Program to check if a string is a Pallindrome or Not.

def fun(a):
    rev=a[::-1]

    if(a==rev):
        print("Yes")
    else:
        print("No")
x=input("Enter a String: ")
if fun(x):
    print("It is NOT a Palindrome")        
else:
    print("It is a Palindrome")