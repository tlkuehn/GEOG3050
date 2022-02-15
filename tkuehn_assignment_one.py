######################################################################
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
#
# Note: Your hawkid is the login name you use to access ICON, and NOT
# your firstname-lastname@uiowa.edu email address.
#
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
######################################################################
def hawkid():
    return(["Tabitha Kuehn", "tkuehn"])

######################################################################
# DON'T MAKE ANY CHANGES HERE.
if (not hawkid()[0] or not hawkid()[1]) or (hawkid()[1] == "hawkid"):
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
    print('### Otherwise, the Autograder will assign 0 points.')
    exit(-1)
else:
    info = hawkid()
    print(info[0])
    print(info[1])
######################################################################

######################################################################
# Problem 1 - Getting Input - (8 Points)
#
# Specification: You are expected to ask for three main inputs:
#     1. mode: This input will be a string given by the user to determine
#              the calculation method. Valid inputs are 'min', 'max', 'avg'.
#     2. count: This input will be an integer given by the user to indicate
#               how many more inputs/values are expected to be given. These
#               new values will be added to a list to be used later in the
#               calculations.
#     3. values: These inputs will be floats. You are expected to read user
#                input 'count' times to get all the values. All of the values
#                should be stored in a list to be used later.
#
# What is expected?
#     After you get all the inputs from the user, print the following information
#     in order:
#           - Print 'mode' variable value (1 Point)
#           - Print 'count' variable value (1 Point)
#           - Print length of the list you have just created (1 Point)
#           - Print the list you have just created (5 Points)
#     All of the prints should be in separate print statements. Please, don't
#     forget that the order is very important.
#
# Note: Don't forget that input() function returns a string, not a number
#       even though you give a number as an input. Therefore, be careful
#       about data type conversions.
#
# Example Input/Output:
#     Assume that you are given the following inputs:
#       avg
#       4
#       123
#       14234
#       25435
#       14
#
#     Your solution for Problem 1 should print the following:
#       Caglar Koylu (Your name will be here)
#       ckoylu (Your hawkid will be here)
#       avg
#       4
#       4
#       [123.0, 14234.0, 25435.0, 14.0]
######################################################################


input_mode =input('Enter min, max, or avg: ')
print(input_mode)
input_count = input('Enter number of values that will be given: ')
print(input_count)
input_values = input('Enter all values seperated by a space: ')
value_list = input_values.split()
for element in range(len(value_list)):
    value_list[element] = float(value_list[element])
print(len(value_list))
print(value_list)



######################################################################
# Problem 2 - Find the Minimum/Maximum/Average - (12 Points)
#
# Specification: In this part of the homework, you are expected to compute
# a value for the given 'mode'. Therefore, your code has to have three main
# code blocks:
#     1. Finding Minimum: If the value of 'mode' is 'min', find the minimum
#                         element in the list. Then, print its value.
#     2. Finding Maximum: If the value of 'mode' is 'max', find the maximum
#                         element in the list. Then, print its value.
#     3. Finding Average: If the value of 'mode' is 'avg', compute the average
#                         of all elements in the list. Computation is basically:
#                               (Sum of all elements)/(Number of elements)
#
# Note: BE CAREFUL. YOU CANNOT USE ANY LIBRARIES OR PYTHON'S BUILT-IN
#       min, max, sum operations. You are expected to implement these operations
#       by your own. Such an use of those functions are not allowed and may cause
#       you loose points.
#
# Hint: These three code blocks depend on the value of 'mode'. Therefore,
#       using a conditional branches may help you to perform different
#       operations in different code blocks. Also, in order to traverse
#       over each element in the list one by one iteration concepts can
#       be very helpful.
#
# Example Input/Output:
#     Assume that you are given the following inputs:
#       avg
#       4
#       123
#       14234
#       25435
#       14
#
#     Your solution for Problem 1 & 2 should print the following:
#       Caglar Koylu (Your name will be here)
#       ckoylu (Your hawkid will be here)
#       avg
#       4
#       4
#       [123.0, 14234.0, 25435.0, 14.0]
#       9951.5
######################################################################


# WRITE YOUR SOLUTION FOR PROBLEM 2 HERE.

# FINDING MINIMUM
if input_mode == 'min':
    minimum = value_list[0]
    for element in range(1, len(value_list)):
        if (value_list[element] < minimum):
            minimum = value_list[element]
    print(minimum)

# FINDING MAXIMUM
if input_mode == 'max':
    maximum = value_list[0]
    for element in range(1, len(value_list)):
        if (value_list[element] > maximum):
            maximum =  value_list[element]
    print(maximum)

# FINDING AVERAGE
if input_mode == 'avg':
    added_values = 0
    for element in value_list:
        added_values += element
        average = added_values/len(value_list)
    print(average)

    



######################################################################

