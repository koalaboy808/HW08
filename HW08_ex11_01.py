#!/usr/bin/env python
# Exercise 1  
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn t matter what the 
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
##############################################################################

def store_to_dict():

	with open("words.txt") as f_in:
        # read each line of the text file and save into list formate
		store_list = [line.strip() for line in f_in]
        # make dictonary using store_list as keys, and length as the values
		make_dict = {name:len(name) for name in store_list}
		return make_dict



##############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print "Yup."
    if "qwertyuiop" in words_dict:
        print "Hmm."

if __name__ == '__main__':
    main()
