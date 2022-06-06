
### continue statement

### only print odd numbers from 0-10
for number in range(0, 11):
    if number % 2 == 0:
        continue
    print(number)

### break statement
### print number till 5

for number in range(0, 11):
    if number > 5:
        break
    print(number)

numbers = [1,2,3,4,5]
for value in numbers:
    if value % 2 is not 0:
        break

# using break within function
def check_google_employee(companies):
    is_google_employee = False

    for company in companies:
        if company == "google":
            is_google_employee = True
            break

    if is_google_employee == True:
        return "You are in google!!"
    else:
        return "You are not in google!!"

companies = ["nagaro", "one97", "yahoo"]
print(check_google_employee(companies))
