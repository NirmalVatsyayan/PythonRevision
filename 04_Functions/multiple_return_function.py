
def name_metadata(first_name, last_name):
    """returns full name and length of full name"""

    full_name = first_name + " " + last_name
    full_name_length = len(full_name)
    return full_name, full_name_length


output, output_length = name_metadata("ashish", "jain")
print("full name is ", output)
print("full name length is ", output_length)
