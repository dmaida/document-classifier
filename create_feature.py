import processing
import pickle
import os
import sys

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

	dr_word_list = []
	dt_word_list = []
	l_word_list = []
	words = ''
	for f in dr_files:
		words += processing.processing(os.path.join(dr_path, f))
	print(words)
if __name__ == '__main__':
	main(sys.argv)
