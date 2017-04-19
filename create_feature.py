import processing
import pickle
import os
import sys

def get_frequency(path, file_list):
	words = ''
	for f in file_list:
		words += processing.processing(os.path.join(base_path, f))
	words = words.split() #splits into list on whitespace
	total_num_words = len(words)

def main(argv):
	base_path = argv
	print(argv)
	if len(argv) != 2:
		base_path = 'data'
	dr_path = os.path.join(base_path,'DR')
	dt_path = os.path.join(base_path, 'DT')
	l_path = os.path.join(base_path, 'L')

	dr_files = [f for f in os.listdir(dr_path) if os.path.isfile(os.path.join(dr_path, f))]
	dt_files = [f for f in os.listdir(dt_path) if os.path.isfile(os.path.join(dt_path, f))]
	l_files = [f for f in os.listdir(l_path) if os.path.isfile(os.path.join(l_path, f))]

	dr_word_list = get_words(dr_path, dr_files)
	dt_word_list = get_words(dt_path, dt_files)
	l_word_list = get_words(l_path, l_files)
	
if __name__ == '__main__':
	main(sys.argv)
