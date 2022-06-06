
'''
stack - function, local variables
heap - objects
BSS - global variables
text - code
'''

class Employee:

    def __init__(self):
        self.__age = 0
        self.__name = ""
        self.__employee_id = 0
        self.__joinging_ddmmyy = []

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_emplyee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_joining_date(self, dd, mm, yy):
        self.__joinging_ddmmyy = [dd, mm, yy]

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_joining_date(self):
        return self.__joinging_ddmmyy

# create object
obj = Employee()

# set values
obj.set_age(18)
obj.set_name("deepak")
obj.set_emplyee_id(100)
obj.set_joining_date(10, 11, 2022)

# get values
print(obj.get_name())
print(obj.get_joining_date())


obj_second = Employee()
obj_second.set_age(19)
obj_second.set_name("kuldeep")
obj_second.set_emplyee_id(101)
obj_second.set_joining_date(11, 11, 2022)

# get values
print(obj_second.get_name())
print(obj_second.get_joining_date())
