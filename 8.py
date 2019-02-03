num = int(input("Enter Number To be Checked"))
temp = num
arm=0

while temp>0:
    rem = temp%10
    arm+= (rem*rem*rem)
    temp=temp//10

if(arm==num):
    print("True")
else:
    print("False")
    
