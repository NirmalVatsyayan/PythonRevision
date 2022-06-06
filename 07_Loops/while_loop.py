
# graceful exit from while loop

number = 5
while number > 0:
    print("number is", number)
    number -= 1

# forceful exit from while loop
number = 100
while number > 0:
    print("number is", number)
    number -= 1
    if number < 90:
        break
