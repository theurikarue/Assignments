#Theuri Bonface Karue 
#SCT211-0573/2022

#Tip calculator
#Create a tip calculator that takes in the total bill amount, the tip amount as a percentage of the total bill amount (10,12 or 15 should be the options) and the number of people splitting the bill. After getting these user input values your app should calculate the amount each person should pay and display the answer rounded to two decimal points.


 
total_bill= float(input("Enter total amount of bill: " ))

num_of_people = int(input("Enter number of people splitting the bill: "))
while True:
    tip_percentage = int(input("Enter the percentage you want to use for your tip: "))
    if tip_percentage == 10|12|15:
        break 
    else:
        print("INVALID INPUT!!! ")


tip_amount = total_bill * (tip_percentage/100)
total_tip_inclusive = total_bill + tip_amount
amount_per_person = total_tip_inclusive/num_of_people 


print (f"Each person should pay {amount_per_person}")





