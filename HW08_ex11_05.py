#!/usr/bin/env python
# Exercise 5
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Update print_hist_new from HW08_ex_11_03.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
##############################################################################

def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

# a = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
# print(invert_dict_old(a))

def invert_dict_new(d):
    inverse = dict()
    for key, val in d.items():
        #inverse[val] = inverse.setdefault(val, []) ??? how come don't need to set to value?
       # check to see if val exists as a key using setdefault
       # return empty list if not, or return corresponding values if true
       inverse.setdefault(val, [])
       # append key to inverse
       inverse[val].append(key)
    return inverse


#a = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
#print(invert_dict_new(a))



def print_hist_newest(d):
    # iterate on max key number
    for count in range(max(d.keys())):
        # add 1 to count until max is hit (start at 1)
        count += 1
        # use setdefault to check if key exists... if not create empty list for value pair
        if d.setdefault(count, "Non-Existent!") == "Non-Existent!":
            d[count] = []
    print d


#d = {1:["this, that"], 3: ["the"]}
#print d[3]
#print(print_hist_newest(d))

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_new(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    with open("pledge.txt") as f_in:
        new_list = f_in.read()
        new_list = new_list.split()
        new_list = [word.replace(".","")for word in new_list]
        new_list = [word.replace(":","")for word in new_list]
        new_list = [word.replace(",","")for word in new_list]
        return new_list


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
