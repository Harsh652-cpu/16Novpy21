#program to calculate roots of a quadratic equation
a=int(input("Enter the values of a:"))
b=int(input("Enter the values of b:"))
c=int(input("Enter the values of c:"))
D=(b*b)-(4*a*c)
deno=2*a
if(D>0):
    print("Real Roots")
    root1=(-b+D**0.5)/deno
    root2=(-b-D**0.5)/deno
    print("Root1="+str(root1)+"\tRoot2="+str(root2))
elif(D==0):
    print("Equal roots")
    root=-b/deno
    print("Root1 and Root2="+str(root))
else:
    print("Imaginary roots")