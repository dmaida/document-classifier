import processing
import create_feature
from collections import Counter
import sys

def search(d):
	"""
	Search method for classifying a document based on number of times
	a phrase appears
	"""

	for document in d:
		list_of_words = processing.processing(document)
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
			print (document + ": " + "Deed of Trust\n")

		if dr_freq > l_freq and dr_freq > dt_freq:
			print (document + ": " + "Deed of Reconveyance\n")

		if l_freq > dt_freq and l_freq > dr_freq:
			print (document + ": " + "Lien\n")



		list_of_words = None



def main(argv):
	# run bash$ python3 grep.py path/*
	search(argv)

if __name__ == '__main__':
	main(sys.argv)
