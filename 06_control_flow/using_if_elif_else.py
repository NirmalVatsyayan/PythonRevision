
age = int(input("kindly enter age "))

if age <= 15:
    print("Swimming pool is free for kids !!")
elif age > 15 and age <= 25:
    print("Pay rs. 30 to enter the pool !!")
elif age > 25 and age <= 60:
    print("Pay rs. 100 to enter the pool !!")
else:
    print("Swimming pool is free for senior citizens !!")