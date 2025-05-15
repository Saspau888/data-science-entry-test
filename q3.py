def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.{}
    """
    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


-answer :
def update_dictionary(dct, key, value):
#    print(dct)
#    print(key)
#    print(value)


# find the key value whether it is exist in dct using IF statement.
#if found using dct key abd replace with value    
    if key in dct:
        dct[key] = value
        print(dct)
    else:
#if nothing is found, then it will be replace all the value
        dct[key] = value
        print(dct)

# Example usage
update_dictionary({},"name", "Alice")
update_dictionary({"age": 25}, "age", 26)
