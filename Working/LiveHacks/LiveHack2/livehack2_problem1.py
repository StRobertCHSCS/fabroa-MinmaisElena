'''

-------------------------------------------------------------------------------

Name:       livehack2_problem1.py

Purpose:    To calculate the BMI and display the corresponding message

 

Author: Choi.E

 

Created:    18/11/2019

------------------------------------------------------------------------------

'''
weight = float(input("Enter your weight (kg) : "))
height = float(input("Enter your height (m) : "))
bmi = weight / (height **2)

if (bmi > 25.0):
    print("You are overweight.")
elif (bmi <= 25.0 and bmi >= 18.5):
    print("Your weight is normal.")
else:
    print("You are underweight.")