def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    return


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]


- Answers:

def find_first_negative(lst):

# Using x to capture the len of the lst and using y as initial to carry out the loop and the negative is found, it will break. 
# using else under while and it is not found, it will print no negative found
#		print(lst)
		x = len (lst)
#		print(x)

		y = 0
		while y < x :
#			print(y)
			
			num = lst[y]
#			print(num)
			if num < 0 :
				print (num)
				break
			y = y + 1

		else:
			print ("No negatives")
            
find_first_negative([3, 5, -1, 7, -2, 8])
find_first_negative([2, 10, 7, 0])
