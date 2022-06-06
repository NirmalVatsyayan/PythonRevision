

# Example 1 on string
'''
name = "kuldeep singh ji"

for x in name:
    print(x)

'''

# Example 2 on list
'''
numbers = [1, "prashant", True, [1,2,3], 'x', 10.1]
for x in numbers:
    print(x, "   ", type(x))

print(type(numbers))
'''

# Example 3 on tuple
'''
numbers = (1, "prashant", True, [1,2,3], 'x', 10.1)
for x in numbers:
    print(x, "   ", type(x))


print(type(numbers))
'''

# Example 4 on dictionary
employee_record = {
    "name" : {1:"prashant", 2:"salman", 3:"shahrukh", 4:"johnny depp"},
    "age" : 18,
    "address" : "Noida",
    "is_male" : True,
    "weight" : 65.5,
    (1,2,3) : 1
}
# keys must be unique
# keys must be immutable

#print(employee_record)
#print(type(employee_record))

#for x in employee_record:
#    print(x)

#for x, y in employee_record.items():
#    print("key is ", x, " |||  value is ", y)


'''
x = [ 1, 10.1, True, [1,2,3], (4,5,6) ]

for data in x:
    if isinstance(data, bool):
        print("data is boolean ", data)
    elif isinstance(data, int):
        print("data is integer  ", data)
    elif isinstance(data, float):
        print("data is float ", data)
    elif isinstance(data, list):
        print("data is list ", data)
    else:
        print("data is something else ", data)

'''


print(isinstance(1, int))

