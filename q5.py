def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3


- Answer --
def check_divisibility(num, divisor):

#	print(num, divisor)
# using formula % to check whether there is any remainder value, if there isnt, meaning number is divisible or it is not
	x = num % divisor
	
	if x == 0:
		print("True")
	else:
		print("False")


check_divisibility(10,2)
check_divisibility(7,2)