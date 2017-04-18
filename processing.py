import re
import sys

def processing(f_in):
	"""
	Processes a file by doing 3 operations:
	1) puts all letters in lowercase
	2) removes all non ascii characters and replaces them with spaces
	3) compresses all spaces to a single space
	"""
	f_in = open(f_in, 'r')
	input_string = f_in.read() #read in
	input_string = input_string.lower() #to lower case
	input_string = re.sub("[^0-9a-z]+", ' ', input_string)
	input_string = re.sub('\s+', ' ', input_string).strip() #compresses spaces
	print(input_string)

def main(argv):
	"""
	Main method for running program
	Interprets a single command line arg for text processing
	"""
	if len(argv) < 2:
		print("Must provide a file as an argument")
		return
	if len(argv) > 2:
		print("Must procide only one argument for processing")
		return
	processing(argv[1])

if __name__ == '__main__':
	main(sys.argv)