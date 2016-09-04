#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -! Written In PSCP !-

"""
A module containing bits of code I use a lot
The goal is to help me be able to use less code and spend less time re-writing
already used code
"""

version = "1.0"
status = "Production"

import sys

# shows all the commands in the module and a description of what they do
def provision_help():
	print("'printf' prints the input on the screen without any trailing newline or spaces")
	print("'outf' is a simple function that just returns the input.  Used to test ThreeX3, FourX4, and XXY")
	print("'RunFunction' takes a function and arguments in as input, runs, and returns the output")
	print("'ThreeX3' takes a function and one argument in as input, runs, and returns the output in a 3x3 box")
	print("'FourX4' takes a function and one argument in as input, runs, and returns the output in a 4x4 box")
	print("'XXY' (X by Y) takes a function, one argument, and the box size in as input, runs, and returns the output in the XxY box")


# printf prints the input on the screen without any trailing newline or spaces
def printf(IO):
	sys.stdout.write(str(IO))
	sys.stdout.flush()

# outf is a simple function that just returns the input.  Used to test ThreeX3, FourX4, and XXY
def outf(IO):
	return IO

# RunFunction takes a function and arguments in as input, runs, and returns the output
def RunFunction(function, *args, **kwargs):
	return function(*args, **kwargs)

# ThreeX3 takes a function and one argument in as input, runs, and returns the output in a 3x3 box
def ThreeX3(func, args=None):
	def NoneTypeError():
		print("")
		print("[ERROR] The inputed function doesn't return a output.")
		print("[RESULT] The ThreeX3 function has no use in this context.")

	for i in range(3):
		for i in range(3):
			if (args==None):
				out = RunFunction(func)
				if (out == None): 
					NoneTypeError()
					return 0
				else: printf(out);
			else:
				out = RunFunction(func, args)
				if (out == None): 
					NoneTypeError()
					return 0
				else: printf(out);
		print("")

# FourX4 takes a function and one argument in as input, runs, and returns the output in a 4x4 box
def FourX4(func, args=None):
	def NoneTypeError():
		print("")
		print("[ERROR] The inputed function doesn't return a output.")
		print("[RESULT] The FourX4 function has no use in this context.")

	for i in range(4):
		for i in range(4):
			if (args==None):
				out = RunFunction(func)
				if (out == None): 
					NoneTypeError()
					return 0
				else: printf(out);
			else:
				out = RunFunction(func, args)
				if (out == None): 
					NoneTypeError()
					return 0
				else: printf(out);
		print("")

# XXY (X by Y) takes a function,one argument, and the box size in as input, runs, and returns the output in the XxY box
def XXY(x, y, func, args=None):
	def NoneTypeError():
		print("")
		print("[ERROR] The inputed function doesn't return a output.")
		print("[RESULT] The XXY function has no use in this context.")

	for i in range(y):
		for i in range(x):
			if (args==None):
				out = RunFunction(func)
				if (out == None): 
					NoneTypeError()
					return 0
				else: printf(out);
			else:
				out = RunFunction(func, args)
				if (out == None): 
					NoneTypeError()
					return 0
				else: printf(out);
		print("")

