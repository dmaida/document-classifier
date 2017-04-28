import grep
import bayes
import perceptron
import create_feature
import sys
import os



def main(argv):

	output = open("output.txt", "w")

	print ("Processing Intelli-Grep...")
	grep_dict = grep.search(os.path.join(argv[1] , "TEST"))
	for key, val in grep_dict.items():
		output.write("Intelli-Grep," + key + "," + val + "\n")
		#print("Intelli-Grep," + key + "," + val )

	print("Finished Intelli-Grep\n")



	documents = create_feature.create_naive_document_dictionaries_from_training_files('data')
	test_docs = create_feature.get_documents_from_folder(os.path.join('data', 'TEST'))

	print("Processing Naive Bayes...")
	bayes_dict = bayes.naive_bayes(documents, test_docs)
	for key, val in bayes_dict.items():
		output.write("Naive Bayes," + key + "," + val + "\n")
		#print("Naive Bayes," + key + "," + val)

	print("Finished Naive Bayes\n")


	print("Processing Perceptron...")
	features = list(dict.fromkeys(create_feature.create_boolean_feature_set(documents,drop_short=True) ))
	training_set = perceptron.create_training_set()
	DR_p = perceptron.perceptron('DR',features) #DR perceptron
	DT_p = perceptron.perceptron('DT',features)
	L_p = perceptron.perceptron('L',features)
	DR_p._training(training_set)
	DT_p._training(training_set)
	L_p._training(training_set)
	perceptron_dict = perceptron.testing(DR_p, DT_p, L_p, os.path.join(argv[1] , "TEST"))

	for key, val in perceptron_dict.items():
		output.write("Perceptron," + key + "," + val + "\n")
		#print("Perceptron," + key + "," + val)		

	print("Finished Perceptron")

	output.close()
	


if __name__ == '__main__':
	main(sys.argv)

