#program to read the numbers until -1 is encountered.Find the average of positive numbers and negatives numbers entered by the user
neg_count=0#Total number of negative numbers entered by the user
neg_s=0#The sum of negative number,like neg_s+num and as neg_s is already 0 declared so the neg_s i.e negative sum will be sum of the numbers.Hence now we know the sum of negative numbers and total count of negative numbers.For example we first give -3 then -6 now count will be 2 and neg_s will be -9 so now we can easily find the average of both negative numbers as well as positive numbers.
pos_count=0#Total number of positive values entered by the user
pos_s=0#Sum of all positive numbers by means of which we can find average of +ve numbers easily and accurately
print("Enter -1 to exit...")
num=int(input("Enter the number:"))
while(num!=-1):
    if(num<0):
     neg_count=neg_count+1
     neg_s=neg_s+num
    else:
        pos_count=pos_count+1
        pos_s=pos_s+num
num=int(input("Enter the number:"))
neg_avg=float(neg_s)/neg_count
pos_avg=float(pos_s)/pos_count
print("The average of negative numbers is:"+str(neg_avg))
print("The average of positive numbers is:"+str(pos_avg))