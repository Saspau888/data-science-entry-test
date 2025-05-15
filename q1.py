def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17


- Answer-
def swap(x, y):
# check whether the x and y whether it is integer value if yes, swap x with y and y with x
    if (isinstance(x, int) and isinstance (y, int)):
        x, y = y, x
        print ("Swap value" , x, y)
                
    else:
        print("Unsupported data type", x, y)
        return -1
    

print(swap("Apple",10))
print(swap(9,17))
