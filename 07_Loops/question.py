
def variadic_sum_name(*args):
    sum_args_name = "Prefred Location : "
    #since only 1 argument is passed, i.e a list so lets get it from args
    data = args[0]
    print("len of args", len(args), " value in args ", args)
    print("len of data", len(data), " value in data", data)
    for value in data:
        sum_args_name += " "+value
    return sum_args_name


# take input from user, count of how many locations user want to enter
location_count = input("How many locations you want to enter : ")

# type cast location_count to int
location_count = int(location_count)

# create empty list to hold all locations
locations = []
# run loop to take desired number of inputs from user
for i in range(location_count):
    # get location from user
    l = input("Enter the Prefered Location :")
    # add location in list
    locations.append(l)

print(variadic_sum_name(locations))
