#get the number of students and pieces of chicken
#compute the pieces of chicken that each student will get and the remainders which mr fabora will get.
#output the pieces per student and chicken for mr Fabroa
'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Compute the number of chicken per person / for mr Fobroa

Author:		Elena.C

Created:	02/10/2019
------------------------------------------------------------------------------
'''

student = int(input("Enter the number of sutdents you have got : "))
chicken = int(input("Enter the number of chickens you have got : "))
chickenPerPerson = round(chicken / student, 0)
chickenForMrFabora = chicken % student
print("Each student will get " + str(chickenPerPerson) + " pieces of chicken")
print("Mr.Fabroa will get " + str(chickenForMrFabora) + " pieces of chicken")