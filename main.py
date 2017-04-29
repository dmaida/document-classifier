import grep
import bayes
import perceptron
import create_feature
import sys
import os



def main(argv):

	base_path = argv[1]

	output = open("output.txt", "w")
	print ("Processing Intelli-Grep...")
	grep_dict = grep.search(os.path.join(base_path , "TEST"))
	for key, val in grep_dict.items():
		output.write("Intelli-Grep," + key + "," + val + "\n")
	print("Finished Intelli-Grep\n")

	documents = create_feature.create_naive_document_dictionaries_from_training_files(base_path)
	test_docs = create_feature.get_documents_from_folder(os.path.join(base_path, 'TEST'))
	
	print("Processing Naive Bayes...")
	bayes_dict = bayes.naive_bayes(documents, test_docs)
	for key, val in bayes_dict.items():
		output.write("Naive_Bayes," + key + "," + val + "\n")
	print("Finished Naive Bayes\n")

	print("Processing Multinomial Naive Bayes...")
	bayes_dict = bayes.naive_bayes(documents, test_docs, nomial_bag_of_words=True)
	for key, val in bayes_dict.items():
		output.write("Multinomial_Naive_Bayes," + key + "," + val + "\n")
	print("Finished Multinomial Naive Bayes\n")


	print("Processing Perceptron...")
	perceptron_dict = perceptron.perceptron_classify(documents, base_path)
	for key, val in perceptron_dict.items():
		output.write("Perceptron," + key + "," + val + "\n")
	print("Finished Perceptron")

	print("Processing Naive Bayes with dropping short words improvement...")
	bayes_dict = bayes.naive_bayes(documents, test_docs,drop_short=True)
	for key, val in bayes_dict.items():
		output.write("Naive_Bayes_with_dropped_short_words," + key + "," + val + "\n")
	print("Finished Naive Bayes with dropped short words\n")

	print("Processing Perceptron with dropping short words improvement...")
	perceptron_dict = perceptron.perceptron_classify(documents, base_path, drop_short=True)
	for key, val in perceptron_dict.items():
		output.write("Perceptron_with_dropped_short_words," + key + "," + val + "\n")
	print("Finished Perceptron with dropped short words")

	print("Processing Naive Bayes with dropping common words improvement...")
	bayes_dict = bayes.naive_bayes(documents, test_docs, drop_common_words=True)
	for key, val in bayes_dict.items():
		output.write("Naive_Bayes_with_dropped_common_words," + key + "," + val + "\n")
	print("Finished Naive Bayes with dropped common words\n")

	print("Processing Perceptron with dropping common words improvement...")
	perceptron_dict = perceptron.perceptron_classify(documents, base_path, drop_common_words=True)
	for key, val in perceptron_dict.items():
		output.write("Perceptron_with_dropped_common_words," + key + "," + val + "\n")
	print("Finished Perceptron with dropped common words")

	print("Processing Naive Bayes with dropping stop words improvement...")
	bayes_dict = bayes.naive_bayes(documents, test_docs, drop_stop_words=True)
	for key, val in bayes_dict.items():
		output.write("Naive_Bayes_with_dropped_stop_words," + key + "," + val + "\n")
	print("Finished Naive Bayes with dropped stop words\n")

	print("Processing Perceptron with dropping stop words improvement...")
	perceptron_dict = perceptron.perceptron_classify(documents, base_path, drop_stop_words=True)
	for key, val in perceptron_dict.items():
		output.write("Perceptron_with_dropped_stop_words," + key + "," + val + "\n")
	print("Finished Perceptron with dropped stop words")

	output.close()
	


if __name__ == '__main__':
	main(sys.argv)

