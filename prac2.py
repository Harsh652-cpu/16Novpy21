#program to take input from the user and then checks whether it is a number or a character.If it is a character,determine whether it is in uppercase or lowercase
ch=input("Enter the character:")
if(ch>="A" and ch<="Z"):
    print(str(ch)+" is an uppercase character")
elif(ch>='a' and ch<='z'):
    print(str(ch)+" is a lowercase character")
else:
    if(ch.isdigit()):
        print(str(ch)+" is a digit")