import re

def processing(f_in):
	"""
	Processes a file by doing 3 operations:
	1) puts all letters in lowercase
	2) removes all non ascii characters and replaces them with spaces
	3) compresses all spaces to a single space
	"""
	input_string = f_in.read() #read in
	input_string = input_string.lower() #to lower case
	input_string = re.sub("[^0-9a-z]+", ' ', input_string)
	input_string = re.sub('\s+', ' ', input_string).strip() #compresses spaces
	print(input_string)
	
def main():
	print("I am main")

if __name__ == '__main__':
	main()