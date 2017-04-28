import processing
import create_feature
import re
import random
from collections import Counter
import sys
import os

def search(d):
	"""
	Search method for classifying a document based on number of times
	a phrase appears
	"""

	my_dict = {}

	for document in os.listdir(d):
		list_of_words = processing.processing(os.path.join(d,document))
		list_of_words = list_of_words.split()
		total_num_words = len(list_of_words)
		word_dict = dict(Counter(list_of_words))
		l_freq = 0
		dt_freq = 0
		dr_freq = 0
		if "lien" in word_dict:
			l_freq = word_dict["lien"]

		if "trust" in word_dict:
			dt_freq = word_dict["trust"]

		if "reconveyance" in word_dict:
			dr_freq = word_dict["reconveyance"]

		if dt_freq > l_freq and dt_freq > dr_freq:
			my_dict[re.sub('(.)*(\/)+','',document)] = "DT"
			#print (document + ": 	" + "Deed of Trust\n")

		elif dr_freq > l_freq and dr_freq > dt_freq:
			my_dict[re.sub('(.)*(\/)+','',document)] = "DR"
			#print (document + ": " + "Deed of Reconveyance\n")

		elif l_freq > dt_freq and l_freq > dr_freq:
			my_dict[re.sub('(.)*(\/)+','',document)] = "L"
			#print (document + ": " + "Lien\n")

		else:
			choices = ['DT', 'DR', 'L']
			my_dict[re.sub('(.)*(\/)+','',document)] = random.choice(choices)



		list_of_words = None

	#print (my_dict)
	#create_feature.accuracy_of_results(my_dict, "data/test-results.txt")
	return my_dict



def main(argv):
	# run bash$ python3 grep.py path/*
	search(argv)

if __name__ == '__main__':
	main(sys.argv)
