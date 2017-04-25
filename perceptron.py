import processing
import create_feature
import sys
import pickle
import os
from collections import Counter
from random import shuffle

class perceptron():

	def __init__(self, doc_class, feature_set):
		self.doc_class = doc_class
		self.feature_set = {}
		self.bias = 1
		self.alpha = 0.1
		for word in feature_set:
			self.feature_set[word] = 1

	def _freqs(self, word_list):
		"""
		Returns a dictionary of frequencies mapped to each word in the training set 
		"""
		num_words = len(word_list)
		doc_freq = {}
		for key in self.feature_set:
			c = word_list.count(key)
			doc_freq[key] = c/num_words
		return doc_freq


	def _training(self, training_set):
		"""

		"""
		tot_false_neg = 0
		tot_false_pos = 0
		in_score = 0
		for i in range(10):
			shuffle(training_set) #randomly shuffles the training set.  Should happen every iteration
			iter_neg = 0
			iter_pos = 0
			for doc in training_set:
				#print(doc, self.doc_class)
				doc_data = word_bag(doc[0])
				freq = self._freqs(doc_data)
				for f in freq:
					in_score += freq[f]*self.feature_set[f]
				if in_score > 0 and doc[1] != self.doc_class: #false positive
					#print('False positive')
					tot_false_pos += 1
					iter_pos += 1
					self.bias += self.alpha*-1
					for word in self.feature_set:
						if freq[f] != 0: self.feature_set[word] += self.alpha*-1
				elif in_score <= 0 and doc[1] == self.doc_class: #false negative
					#print('False negative')
					tot_false_neg += 1
					iter_neg += 1
					self.bias += self.alpha*1
					for word in self.feature_set:
						if freq[f] != 0: self.feature_set[word] += self.alpha*1
			print('Done with iteration ', i)
			print('Iteration false negative: ', iter_neg)
			print('Iteration false positive: ', iter_pos)
			print('Total false: ', iter_pos+iter_neg)
			self.alpha -= 0.001
		print('Total false negatives: ', tot_false_neg)
		print('Total false positives: ', tot_false_pos)

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

def main():
    path = 'data'
    documents = create_feature.create_naive_document_dictionaries_from_training_files(path)
    features = list(dict.fromkeys(create_feature.create_boolean_feature_set(documents) ))
    training_set = create_training_set()
    print(len(training_set))
    p = perceptron('DR',features) #DT perceptron
    p._training(training_set)

if __name__ == '__main__':
    main()
