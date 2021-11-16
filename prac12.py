#program to read the numbers until -1 is encouratered.Also count the negative,positive,and zeros entered by the user
negatives=positives=zeros=0
print("Enter -1 to exit...")
while(1):
    num=int(input("Enter any number:"))
    if(num==-1):
        break#end the code when user enters -1
    if(num==0):
        zeros=zeros+1
    elif(num>0):
        positives=positives+1
    else:
        negatives=negatives+1
    print("Count of positive numbers entered:"+str(positives))
    print("Count of negatives numbers entered:"+str(negatives))
    print("Count of zeros entered:"+str(zeros))