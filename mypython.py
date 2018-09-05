#!/usr/bin/python

"""
/*********************************************************************
** Author: James Hippler (HipplerJ)
** Oregon State University
** CS 344-400 (Spring 2018)
** Operating System I
**
** Description: Python Exploration (Program Py)
** Due: Monday, May 21, 2018
**
** Filename: mypython.py
**
** Objectives:
** For this assignment, you will create a script in the Python language.
**
** You can read more about Python here:
** http://www.python.org
**
** All execution, compiling, and testing of this script should ONLY be
** done in the bash prompt on our class server!
**
** Your script must satisfy the following requirements:
** 1. Be contained in one single file, called "mypython.py".
** 2. When executed, create 3 files in the same directory as your script,
** each named differently (the name of the files is up to you), which
** remain there after your script finishes executing. Each of these 3
** files must contain exactly 10 random characters from the lowercase alphabet,
** with no spaces ("hoehdgwkdq", for example). The final (eleventh) character
** of each file MUST be a newline character. Thus, running wc (wordcount)
** against your files in the following manner must return 11:
**
**     $ cat myfile
**     gkwjhcfikf
**
**     $ wc -c myfile
**     11 myfile
**
** 3. When executed, output sent to stdout should first print out the
** contents of the 3 files it is creating in exactly the format given below.
** 4. After the file contents of all three files have been printed, print out
** two random integers each on a separate line (whose range is from 1 to 42,
** inclusive).
** 5. Finally, on the last (sixth) line, print out the product of the two numbers.
**
** You do not have to parse and read the data back in from the files created
** in step 2 in order to complete step 3. For step 3, just dump the contents that
** you already randomly generated in your program directly onto the screen, if
** that's the easiest way for you. I recommend that you look into sys.stdout.write()
** for outputting text, as it will allow you to control newlines better.
**
** The graders will simply be checking for the above requirements to assign
** your grade, using the exact format shown below. Further, no help on this
** assignment will be provided by the Instructor or TAs at any time.
**
** You can choose to use Python 2 or Python 3. The TAs will try all three of
** these commands to find one that works with your script:
**
** 	$ python mypython.py
** 	$ python2.7 mypython.py
** 	$ python3 mypython.py
**
** Python is NOT a topic that will be covered on the Final.
**
** EXTERNAL RESOURCES
** https://stackoverflow.com/questions/4283876/how-to-import-part-of-a-module-in-python
** https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case
** -letters-and-digits-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_
** campaign=google_rich_qa
*********************************************************************/
"""

from random import choice														# Import the choice module from the random library
from random import randint														# Import the randint module from the random library
from sys import stdout															# Import the stdout module from the sys library
from string import ascii_lowercase												# Import the ascii_lowercase module from the string library

"""
/************************************************************************
* Description: create_random_strings function
* Function creates strings of 11 characters in length.  The first ten
* characters are random lower case letters and the eleventh character
* is a breakline "\n" to add a newline to the file.  The functions generates
* three of these strings, prints them to the screen and then appends
* them to an array that will be returned to main.
*************************************************************************/
"""

def create_random_strings():
	random_strings = []															# Create an array to store the randomly generated strings
	for x in range (3):															# For loop that will create 3 separate random strings
		random_strings.append(''.join(choice(ascii_lowercase)					# Create the string using the choice library in random to assign lower case ascii variables
		if x < 10 else "\n" for x in range(11)))								# Make the first 10 character random lower case and the last character a new line
		stdout.write(random_strings[x])											# Print the string to the console using sys.stdout.write to avoid printing newlines
	return random_strings														# Return array to main function

"""
/************************************************************************
* Description: create_random_integer function
* Function uses the randint library to create two integers with values
* between 1 and 42.  Appends the integers to an array and returns to
* main function.
*************************************************************************/
"""

def create_random_integer():
	random_integers = []														# Create an array to store the randomly generated integers
	for x in range(2):															# For loop that will create 2 random integers
  		random_integers.append(randint(1,42))									# Randomly create an integers between 1 and 42 and append to array
  		print(random_integers[x])												# Print the integer to the console
  	return random_integers														# Return the integer array to the main function

"""
/************************************************************************
* Description: write_strings function
* Function write the randomly generated strings to three seperate files,
* named randome_string_file_1, random_string_file_2, and random_string_file_3
* It receives the random_strings files from main and returns nothing
*************************************************************************/
"""

def write_strings(random_strings):
	for x in range(len(random_strings)):										# For loop to traverse through the three random strings stored in the array
		with open("random_string_file_{}".format(x + 1), "w") as file:			# Open a file named "random_string_file_(x + 1)" for writing
			file.write(random_strings[x])										# Write the string to the file and close.

"""
/************************************************************************
* Description: get_product function
* Function multiplies the two randomly generated integers in the array
* to find their product and prints the results to the screen.  Receives
* random_integers array and returns nothing.
*************************************************************************/
"""

def get_product(random_integers):
	print(random_integers[0] * random_integers[1])								# Print the product of the two randomly generated integers

"""
/************************************************************************
* Description: main function
* Calls functions necessary for generating, displaying, and writing
* three random strings and two random integers.
*************************************************************************/
"""

def main():
	write_strings(create_random_strings())										# Call the function to write strings, give it the return from the function to create strings
	get_product(create_random_integer())										# Call function to multiply integers, give it the return value from the function to create integers

if __name__ == "__main__":
	main()																		# Call the main function to begin the program
