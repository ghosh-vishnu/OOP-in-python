# Write A program to check prime number or not
 
num=int(input("Enter Your Number: "))

if num ==1:
    print("This is Not a Prime Number")
for i in range(2,num):
    if num %i==0:
        print(num,"is Not Prime Number")
        break
    else:
        print(num,"This is a Prime Number")
        break