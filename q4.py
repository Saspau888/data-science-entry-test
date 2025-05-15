def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"


- Answer:
def string_reverse(s):

	reverse = ""
	x = len(s)
#	print(x)
#	print(s)

# Using x to capture total len of s.
# Using backward calculation from last character to the first character and capture using variable reverse and join one at a time   
	while x>0:
		character = s[x-1]
		x = x - 1
#		print(character)
		reverse = reverse + character
#		print(reverse)
	else:
		print(reverse)

string_reverse("Hello World")
string_reverse("Python")