import sys


age = int(input("kindly enter age "))
gender = input("kindly enter gender ")

#if gender is not "M" or gender is not "F":
if gender not in ["M", "F"]:
    print("invalid gender entered")
    sys.exit(1)

if age <= 15:
    if gender == "F":
        print("Pool is free for girls !!")
    else:
        print("Pool is free for boys !!")
elif age > 15 and age <= 60:
    if gender == "F":
        print("Charges of pool is rs 50 for women !!")
    else:
        print("You are not allowed !!")
else:
    print("Pool is free for senior citizens !!")


