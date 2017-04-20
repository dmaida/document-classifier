import processing
import pickle
import os
import sys
from collections import Counter

"""Creates a boolean bag of words feature set"""
def create_navie_boolean_feature_set(training_path):
	dr_freq, dt_freq, l_freq = get_naive_frequency_from_training_files(training_path)
	#combines the lists
	feature_words = [ x[0] for x in dr_freq ] + [ x[0] for x in dt_freq ] + [ x[0] for x in l_freq ]
	#The set gets rid of duplicates, then it makes a dictionary for a bag for word
	return dict.fromkeys(set(feature_words))

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
def create_document_dictionaries_from_training_files(base_path):

	dr_files = [f for f in os.listdir(dr_path) if os.path.isfile(os.path.join(dr_path, f))]
	dt_files = [f for f in os.listdir(dt_path) if os.path.isfile(os.path.join(dt_path, f))]
	l_files = [f for f in os.listdir(l_path) if os.path.isfile(os.path.join(l_path, f))]
	dr_documents = dt_documents = l_documents = {}
	for f in dr_files:
		dr_documents[f] = processing.processing(os.path.join(base_path,f))

def get_naive_frequency_from_training_files(base_path):

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
	return [dr_freq, dt_freq, l_freq]

def main(agrv):
	if len(argv) != 2:
		base_path = 'data'
	else:
		base_path = argv[1]
	get_naive_frequency_from_training_files(base_path)
if __name__ == '__main__':
	main(sys.argv)
