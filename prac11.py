#Program to calculate the sum of numbers from m to n.
m=int(input("Enter the value of m:"))
n=int(input("Enter the values of n:"))
s=0
while(m<=n):
    s=s+m
    m=m+1
print("Sum="+str(s))