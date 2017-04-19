import processing
import pickle
import os
import sys
from collections import Counter

def get_frequency(path, file_list):
	words = ''
	for f in file_list:
		words += processing.processing(os.path.join(path, f))
	words = words.split() #splits into list on whitespace
	total_num_words = len(words)
	word_dict = dict(Counter(words))
	frequency_list = list({w: c/total_num_words for w,c in word_dict.items()}.items())
	#print(frequency_list)
	sorted_freq_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)
	return sorted_freq_list[0:20]

def main(argv):
	if len(argv) != 2:
		base_path = 'data'
	else:
		base_path = argv[1]
	dr_path = os.path.join(base_path,'DR')
	dt_path = os.path.join(base_path, 'DT')
	l_path = os.path.join(base_path, 'L')

	dr_files = [f for f in os.listdir(dr_path) if os.path.isfile(os.path.join(dr_path, f))]
	dt_files = [f for f in os.listdir(dt_path) if os.path.isfile(os.path.join(dt_path, f))]
	l_files = [f for f in os.listdir(l_path) if os.path.isfile(os.path.join(l_path, f))]

	dr_freq = get_frequency(dr_path, dr_files)
	dt_freq = get_frequency(dt_path, dt_files)
	l_freq = get_frequency(l_path, l_files)
	print(dr_freq)
	print(dt_freq)
	print(l_freq)

if __name__ == '__main__':
	main(sys.argv)
