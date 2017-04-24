import processing
import create_feature
import sys
import pickle
import os
from collections import Counter

class perceptron():

	def __init__(self, doc_class, feature_set):
		self.doc_class = doc_class
		self.feature_set = {}
		self.bias = 1
		self.alpha = 0.1
		for word in feature_set:
			self.feature_set[word] = 1

	def _freqs(self,):
		"""
		should get freqs for all words in training set
		"""

	def _training(self, training_set):
		"""

		"""
		in_score = 0



def word_bag(f_path):
	"""
	Creates "bag of words" over a given document
	"""
	raw_data = processing.processing(f_path)	
	data_list = raw_data.split()
	return data_list

	
def create_training_set():
	base_path = 'data'
	dr_path = os.path.join(base_path,'DR')
	dt_path = os.path.join(base_path, 'DT')
	l_path = os.path.join(base_path, 'L')
	
	training_list = []
	for f in os.listdir(dr_path):
		training_list.append((os.path.join(dr_path, f), 'DR'))
	for f in os.listdir(dt_path):
		training_list.append((os.path.join(dt_path, f), 'DT'))
	for f in os.listdir(l_path):
		training_list.append((os.path.join(l_path, f), 'L'))
		
	return training_list

def main(argv):
    print(argv)

if __name__ == '__main__':
    main(sys.argv)
