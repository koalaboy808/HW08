'''
Bulls and Cows

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
		digits_allowed = 3
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

def bulls_cows(user_input, magic_number):
	# convert input and magic to string lists
	input_list = [i for i in str(user_input)]
	magic_list = [i for i in str(magic_number)]

	# insert i number of '0's in both lists for the number of digits that begin with int 0 
	open_input = digits_allowed() - len(input_list)
	[input_list.insert(0, '0') for i in range(open_input)]

	magic_input = digits_allowed() - len(magic_list)
	[magic_list.insert(0, '0') for i in range(magic_input)]

	# create empty list for following loops
	temp_list = []

	# first create cow placeholders for temp_list as bull takes precedence
	for i in range(len(input_list)):
		# if any userinput digit matches, then append 'cow' for that index
		if input_list[i] in magic_list:
			temp_list.append('cow')
		# otherwise append None
		else:
			temp_list.append(None)

	# create bull placeholders for temp_list
	for i in range(len(input_list)):
		# if userinput digit matches exact index digit, then replace index with 'bull'
		if input_list[i] == magic_list[i]:
			temp_list[i] = ('bull')

	# create bull_cow dictionary with keys (None, cow and bull) all set to value (0)
	bc_dict = {None: 0, "cow": 0, "bull": 0}
	# loop through the temp_list to get count of cow and bull appearances
	for i in temp_list:
		bc_dict[i] = bc_dict.get(i,0) + 1

	print str(bc_dict['bull']) + " bull(s), " + str(bc_dict['cow']) + " cow(s). Try again: "


def user_input():
	# guesses will be a counter for the number of guesses user has made
	guesses = 1
	# call random integer function to create the magic number user needs to guess
	magic_number = random_integer()

	# maxinum of rounds allowed
	max_number = (2**digits_allowed())+digits_allowed()
	print "You have " + str(max_number) + " tries... or else GAME OVER!"

	# create while True loop until user finally guesses the magic number
	while True:
		if guesses > max_number:
			print "Sorry. You did not guess the number in " + str(max_number) + " tries. The correct number is " + str(magic_number)
			break
		else:
			user_input = raw_input("Enter a " + str(digits_allowed()) + "-digit number: \n")
			# check to see if user_input is a number
			try:
				int(user_input)
			# except will catch all non-integer valus
			except:
				print("This isn't even a number...provide a " + str(digits_allowed()) +"-digit number")
			# else will only evaluate once user has properly input an integer
			else:
				# if statement runs if the length of user input is the number of digits allowed
				if len(user_input)==digits_allowed():

						user_input = int(user_input)
						print magic_number

						# checks to see if user_input equals magic number
						if user_input == magic_number:
							print "Correct! It took you " + str(guesses) + " guesses to choose the correct number of " + str(magic_number)
							break
						else:
							bulls_cows(user_input, magic_number)
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