import re
import sys
import enchant

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
	#print(input_string)
	return input_string

def preprocessed_data(f_in):
	"""
	Method to read in already processed data
	for time efficiency.
	"""
	f_in = open(f_in, 'r')
	input_string = f_in.read()
	return input_string


def processing_with_autocorrect(f_in):
	"""
	Processing with spell checking.

    Spell checking function that autocorrects
    using the suggestion method in
    the enchant library. The incorrectly spelled
	word is replaced with first suggestion of suggestion()

	Processes a file by doing 3 operations:
	1) puts all letters in lowercase
	2) removes all non ascii characters and replaces them with spaces
	3) compresses all spaces to a single space
    """
	f_in = open(f_in, 'r')
	input_string = f_in.read() #read in

	list_of_words = input_string.split()
	d = enchant.Dict("en_US")

	for i in range(len(list_of_words)):
		if d.check(list_of_words[i]) == False: # if the word is miss spelled
			suggestion = d.suggest(list_of_words[i])
			if suggestion:
				list_of_words[i] = suggestion[0]

	processed_string = ' '.join(list_of_words)

	processed_string = processed_string.lower() #to lower case
	processed_string = re.sub("[^0-9a-z]+", ' ', processed_string)
	processed_string = re.sub('\s+', ' ', processed_string).strip() #compresses spaces
	return processed_string

def main(argv):
	"""
	Main method for running program
	Interprets a single command line arg for text processing
	"""
	if len(argv) < 2:
		print("Must provide a file as an argument")
		return
	if len(argv) > 2:
		print("Must provide only one argument for processing")
		return
	processing(argv[1])

if __name__ == '__main__':
	main(sys.argv)
