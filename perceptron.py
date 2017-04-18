import processing
import sys
from collections import Counter

def perceptron():
    print("test")

def word_bag(data):
	"""
	Creates "bag of words" over a given document
	"""
	data_list = data.split()
	data_dict = dict(Counter(data_list))
def main(argv):
    print(argv)

if __name__ == '__main__':
    main(sys.argv)
