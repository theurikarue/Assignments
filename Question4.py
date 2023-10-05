#Theuri Bonface Karue 
#SCT211-0573/2022


#Create an app that takes an year as the input and informs you whether it is a leap year or not.

year = float(input("Enter the year you want to confirm: "))

if year % 4 == 0:
    print("This is a leap year.")
else:
    print ("This is NOT a leap year.")

