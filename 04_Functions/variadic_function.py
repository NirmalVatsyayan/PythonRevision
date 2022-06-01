
def variadic_sum(*args):
    """variable length arguments in a function"""
    sum_args = 0
    print("length of arguments =", len(args))
    for value in args:
        sum_args += value
        #sum_args = sum_args + value #behaves similarly like above statement

    return sum_args

print(variadic_sum(1))
print(variadic_sum(1, 2))
print(variadic_sum(1, 2, 3))
