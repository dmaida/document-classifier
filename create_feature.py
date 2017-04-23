import processing
import pickle
import os
import sys
from collections import Counter, namedtuple

documentTypes = namedtuple('documentTypes', ['dr', 'dt','l'])

"""Creates a boolean bag of words feature set from the the three different classes of documents
Documents is expect to have to dr, dt, and dt dictionary full their documents
it then combines 20 most frequent words in each class, and removes duplicates to retun a set"""
def create_boolean_feature_set(documents):
	dr_freq, dt_freq, l_freq = get_frequency_from_training_documents(documents)
	#combines the lists
	feature_words = [ x[0] for x in dr_freq ] + [ x[0] for x in dt_freq ] + [ x[0] for x in l_freq ]
	#The set gets rid of duplicates, then it makes a dictionary for a bag for word
	return set(feature_words)

def get_frequency(document_dict):
	words = ''
	for key in document_dict:
		words += document_dict[key]
	words = words.split() #splits into list on whitespace
	total_num_words = len(words)
	word_dict = dict(Counter(words))
	frequency_list = list({w: c/total_num_words for w,c in word_dict.items()}.items())
	#print(frequency_list)
	sorted_freq_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)
	return sorted_freq_list[0:20]
"""Creates a list of dictionaries for each type of doucment that's key is file name, and value is the processed text.
It is returned in a tuple, where documents[0] = dr, documents[1] = dt, documents[2] = l """
def create_naive_document_dictionaries_from_training_files(base_path):
	dr_path = os.path.join(base_path,'DR')
	dt_path = os.path.join(base_path, 'DT')
	l_path = os.path.join(base_path, 'L')

	dr_files = [f for f in os.listdir(dr_path) if os.path.isfile(os.path.join(dr_path, f))]
	dt_files = [f for f in os.listdir(dt_path) if os.path.isfile(os.path.join(dt_path, f))]
	l_files = [f for f in os.listdir(l_path) if os.path.isfile(os.path.join(l_path, f))]

	dr_documents = {}
	dt_documents = {}
	l_documents = {}
	for f in dr_files:
		dr_documents[f] = processing.processing(os.path.join(dr_path,f))
	for f in dt_files:
		dt_documents[f] = processing.processing(os.path.join(dt_path,f))
	for f in l_files:
		l_documents[f] = processing.processing(os.path.join(l_path,f))
	return documentTypes(dr_documents, dt_documents, l_documents)

def get_frequency_from_training_documents(processed_documents):
	dr_freq = get_frequency(processed_documents.dr)
	dt_freq = get_frequency(processed_documents.dt)
	l_freq = get_frequency(processed_documents.l)
	return [dr_freq, dt_freq, l_freq]

def main(argv):
	if len(argv) != 2:
		base_path = 'data'
	else:
		base_path = argv[1]
	get_naive_frequency_from_training_files(base_path)
"""
OLD METHODS That don't keep the documents. Can Delete if Unused
The methods are based on file path
"""
def get_naive_frequency_from_training_files(base_path):
	dr_path = os.path.join(base_path,'DR')
	dt_path = os.path.join(base_path, 'DT')
	l_path = os.path.join(base_path, 'L')

	dr_files = [f for f in os.listdir(dr_path) if os.path.isfile(os.path.join(dr_path, f))]
	dt_files = [f for f in os.listdir(dt_path) if os.path.isfile(os.path.join(dt_path, f))]
	l_files = [f for f in os.listdir(l_path) if os.path.isfile(os.path.join(l_path, f))]

	dr_freq = get_frequency_file(dr_path, dr_files)
	dt_freq = get_frequency_file(dt_path, dt_files)
	l_freq = get_frequency_file(l_path, l_files)
	print(dr_freq)
	print(dt_freq)
	print(l_freq)
	return [dr_freq, dt_freq, l_freq]

def get_frequency_file(path, file_list):
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

def file_create_naive_boolean_feature_set(path):
	dr_freq, dt_freq, l_freq = get_naive_frequency_from_training_files(path)
	#combines the lists
	feature_words = [ x[0] for x in dr_freq ] + [ x[0] for x in dt_freq ] + [ x[0] for x in l_freq ]
	#The set gets rid of duplicates, then it makes a dictionary for a bag for word
	return dict.fromkeys(set(feature_words))


if __name__ == '__main__':
	main(sys.argv)
