def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


-Asnwer:
def find_and_replace(lst,find_val,replace_val):

# Using find_val and find out which index number it is belong to
#then using the same index number and replace with lst index with replace_value       
    index = lst.index(find_val)
    lst[index] = replace_val
    print(lst)
  

# having an empty function definition like this, would raise an error without the pass statement

find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
find_and_replace(["apple", "banana", "apple"], "apple", "orange")