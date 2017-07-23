import os
import datetime

year = datetime.datetime.now()  # getting current year from system

#now calculating the birth year
year_of_birth = int(input("Enter your birth "))

print("Doing magic .. you are %i year old" %(year - year_of_birth))