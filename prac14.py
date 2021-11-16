#program to find whether the given number is an Armstrong number or not?
#Armstrong number:-An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.
#For example,371 is an Armstrong number since 3**3+7**3+1**3=371.
n=int(input("Enter the number:"))
s=0
num=n
while(n>0):
    r=n%10
    s=s+(r**3)
    n=n/10
    if(s==num):
        print("The number is Armstrong number")
    else:
        print("The number is not Armstrong number")