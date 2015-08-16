'''
Example 0:

python mimsmind0.py

'''

##### Import ####

import sys
from random import randint

##### Body ####

# create function to find length of sys.argv input
def digits_allowed():
	# test to see if user input exists
	try:
		digits_allowed = sys.argv[1]
	# if user input does not exist then digits allowed is 1
	except:
		digits_allowed = 1
	# if user input does exist then digits allowed equals length of user input
	else:
		digits_allowed = len(sys.argv[1])
	return digits_allowed

# create a function to produce a random integer
def random_integer():
	# call digits_allowed function
	number_digits = digits_allowed()
	# find max range by executing 10 to the number of digis minus 1
	random_integer = randint(0, (10**number_digits)-1)
	return random_integer


def user_input():
	# forgot the 'while True'... 
	# was trying to re-call user_input() if the input was not what I was looking for
	
	# guesses will be a counter for the number of guesses user has made
	guesses = 1
	# call random integer function to create the magic number user needs to guess
	magic_number = random_integer()

	# create while True loop until user finally guesses the magic number
	while True:
		user_input = raw_input("Enter a " + str(digits_allowed()) + "-digit number: \n")
		# check to see if user_input is a number
		try:
			int(user_input)
		# except will catch all non-integer valus
		except:
			print("This isn't even a number...provide a " + str(digits_allowed()) +"-digit number")
		# else will only evaluate once user has properly input an integer
		else:
			# if statement runs if the length of user input is the number of digits allowed and is a number
			if len(user_input)==digits_allowed():

					user_input = int(user_input)

					# checks to see if user_input equals magic number
					if user_input == magic_number:
						print "Correct! It took you " + str(guesses) + " guesses to choose the correct number of " + str(magic_number)
						break
					elif user_input > magic_number:
						print "too high"
						guesses += 1
					elif user_input < magic_number:
						print "too low"
						guesses += 1
			# else statement runs if the length of user input is NOT the number of digits alloed
			else:
				print("Not a " + str(digits_allowed()) +"-digit number")


##############################################################################
##################### call functions below through main(): ###################
##############################################################################
def main():  
	user_input()

if __name__ == '__main__':
    main()