'''

-------------------------------------------------------------------------------

Name:       livehack3_problem2.py

Purpose:   to calculate the days to surpass 100km and average distance per day

Author: Choi.E

 

Created:    11/12/2019

------------------------------------------------------------------------------

'''
distance_traveled = 0
count = 1
distance_traveled = int(input("Enter the distance traveled for the day: "))
while distance_traveled > 0 and distance_traveled < 100:
    distance_traveled = distance_traveled + int(input("Enter the distance traveled for the day: "))
    count += 1
print("It took " + str(count) + " days to surpass 100km driven.")
print("The average distance driven per day is " + str(distance_traveled/count) + "km.")
    