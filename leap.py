# Write a program to check leap year of not

year=int(input("Enter Your Year: "))
if year%400==0 and year%100==0:
    print(year,"is Leap Year")
elif year%4==0 and year%100!=0:
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")