#write a program to enter the marks of a student in four subjects.Then calculate the total and aggregate,and display
#grade obtained by the student.If the student scores an aggregate greater than 75%,then the grade is Distinction.
#If aggregate is 60>= and <75,then the grade is First Division.If aggregate is 50>= and <60,then the grade is
#second division.If aggregate is 40>= and <50,then the grade is Third division.Else the grade is fail.
sub1=int(input("Enter marks of 1st subject:"))
sub2=int(input("Enter the marks of 2nd subject:"))
sub3=int(input("Enter the marks of 3rd subject:"))
sub4=int(input("Enter the marks of 4th subject:"))
total_marks=sub1+sub2+sub3+sub4
percent=total_marks/4
print(percent)
if(percent>=75):
    print("Distinction")
elif(percent>=60 and percent<75):
    print("First division")
elif(percent>=50 and percent<60):
    print("Second division")
elif(percent>=40 and percent<50):
    print("Third division")
else:
    print("Fail")