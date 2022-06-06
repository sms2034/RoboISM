string = input("Enter a string: ")
alphabets = digits = special = 0

for k in range (len(string)):
    if(string[k].isalpha()):
        alphabets = alphabets +1
    elif(string[k].isdigit()):
        digits = digits +1
    else:
        special = special +1

print("\n Number of alphabets: ",alphabets)
print("\n Number of digits: ",digits)
print("\n Number of special characters: ",special)