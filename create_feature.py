import processing
import pickle
import os
import sys
from collections import Counter, namedtuple
from tabulate import tabulate
# got the stop word list from python libary stop-words, manually adding it the program so we don't have another library dependency, and we only need the english words
stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
documentTypes = namedtuple('documentTypes', ['dr', 'dt','l'])

"""Creates a boolean bag of words feature set from the the three different classes of documents
Documents is expect to have to dr, dt, and dt dictionary full their documents
it then combines 20 most frequent words in each class, and removes duplicates to retun a set"""
def create_boolean_feature_set(documents, drop_short=False, drop_stop_words=False):
	dr_freq, dt_freq, l_freq = get_frequency_from_training_documents(documents,drop_short, drop_stop_words)
	#combines the lists
	feature_words = [ x[0] for x in dr_freq ] + [ x[0] for x in dt_freq ] + [ x[0] for x in l_freq ]
	#The set gets rid of duplicates, then it makes a dictionary for a bag for word
	return set(feature_words)

def get_frequency(document_dict, drop_short=False, drop_stop_words=False):
	words = ''
	for key in document_dict:
		words += document_dict[key]
	words = words.split() #splits into list on whitespace
	total_num_words = len(words)
	word_dict = dict(Counter(words))
	frequency_list = list({w: c/total_num_words for w,c in word_dict.items()}.items())
	#print(frequency_list)

	sorted_freq_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)
	s_copy = sorted_freq_list.copy()
	if drop_short:
		for s in s_copy:
			if len(s[0]) < 3: sorted_freq_list.remove(s)
	s_copy = sorted_freq_list.copy()
	if drop_stop_words:
		for s in s_copy:
			if s[0] in stop_words: sorted_freq_list.remove(s)
	return sorted_freq_list[0:20]

def get_documents_from_folder(path, is_data_preprocessed=False):
	doc_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	doc = {}
	if is_data_preprocessed:
		for f in doc_files:
			doc[f] =  processing.preprocessed_data(os.path.join(path,f))
	else:
		for f in doc_files:
			doc[f] =  processing.processing(os.path.join(path,f))
	return doc

"""Creates a list of dictionaries for each type of doucment that's key is file name, and value is the processed text.
It is returned in a tuple, where documents[0] = dr, documents[1] = dt, documents[2] = l """
def create_naive_document_dictionaries_from_training_files(base_path, is_data_preprocessed=False):
	dr_path = os.path.join(base_path,'DR')
	dt_path = os.path.join(base_path, 'DT')
	l_path = os.path.join(base_path, 'L')

	dr_files = [f for f in os.listdir(dr_path) if os.path.isfile(os.path.join(dr_path, f))]
	dt_files = [f for f in os.listdir(dt_path) if os.path.isfile(os.path.join(dt_path, f))]
	l_files = [f for f in os.listdir(l_path) if os.path.isfile(os.path.join(l_path, f))]

	dr_documents = {}
	dt_documents = {}
	l_documents = {}
	if is_data_preprocessed:
		for f in dr_files:
			dr_documents[f] = processing.preprocessed_data(os.path.join(dr_path,f))
		for f in dt_files:
			dt_documents[f] = processing.preprocessed_data(os.path.join(dt_path,f))
		for f in l_files:
			l_documents[f] = processing.preprocessed_data(os.path.join(l_path,f))
	else:
		for f in dr_files:
			dr_documents[f] = processing.processing(os.path.join(dr_path,f))
		for f in dt_files:
			dt_documents[f] = processing.processing(os.path.join(dt_path,f))
		for f in l_files:
			l_documents[f] = processing.processing(os.path.join(l_path,f))
	return documentTypes(dr_documents, dt_documents, l_documents)

	return documentTypes(dr_documents, dt_documents, l_documents)
def get_frequency_from_training_documents(processed_documents,drop_short=False, drop_stop_words=False):
	dr_freq = get_frequency(processed_documents.dr,drop_short, drop_stop_words)
	dt_freq = get_frequency(processed_documents.dt,drop_short, drop_stop_words)
	l_freq = get_frequency(processed_documents.l,drop_short, drop_stop_words)
	return [dr_freq, dt_freq, l_freq]

def accuracy_of_results(results, answers_path, printTable=False):
	f = open(answers_path, 'r')
	total = len(results)
	correct = 0
	wrong = 0
	# creates a 3x3 for guess and answer grid
	answerGrid = {'DT': {'DT':0, 'DR':0, 'L':0}, 'DR':{'DT':0, 'DR':0, 'L':0}, 'L': {'DT':0, 'DR':0, 'L':0}}

	for line in f:
		document, answer = line.split(',')
		answer = answer.strip()
		document = document.strip()
		if answer == results[document]:
			correct += 1
		answerGrid[answer][results[document]] += 1
	print("Correct: {} Wrong: {} Total: {}".format(correct, total - correct , total))
	print("Precentage: {0:.5f}%".format(float(correct/total*100), "%") )
	#Prints Latex formated data
	if printTable:
		print("Latex Tables")
		tableList = []
		for key in answerGrid:
			tableList.append([key, answerGrid[key]['DT'], answerGrid[key]['DR'], answerGrid[key]['L']])
		print (tabulate(tableList, headers=['DT','DR','L'], tablefmt="latex") )
		print( tabulate([ ["Correct: ", correct], ['Wrong:', total - correct], ['Total', total], ['Percentage:', "{0:.3f}%".format(float(correct/total*100))] ], tablefmt="latex") )
	else:
		print("		   Guessed")
		print('{0}	    {1}     {2}       {3}'.format('Correct', 'DT','DR','L') )
		for key in answerGrid:
			print('      {0}   {1:3d}   {2:4d}   {3:5d}'.format(key.rjust(2),answerGrid[key]['DT'], answerGrid[key]['DR'], answerGrid[key]['L']) )
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
