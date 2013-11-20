#!/usr/bin/python 
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-

'''

Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:


Hello! What is your name?
Torbrn
Well, Torbjorn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!

'''

import random, sys


def guess_number(num):
    random_number = random.randint(1,20)
    if random_number == num:
        print " guess was ok it was" 
	return 1
    else:
        print " U mistake here it was" + str(random_number)
	return 0

if __name__=="__main__":
    
    name = str(raw_input("what is your name ?:"))
    print 
    print "Well"+name+ "I am thinking of a number between 1 and 20."
    for i in range(0, 5):
        num = int(raw_input("Take a  guess \n "))
	result = guess_number(num)
	if result:
	    sys.exit(1)
        
    

