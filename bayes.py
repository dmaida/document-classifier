import create_feature
import sys
import os
import math
from collections import namedtuple

documentTypes = namedtuple('documentTypes', ['dr', 'dt','l'])

def naive_bayes(path):
    documents = create_feature.create_naive_document_dictionaries_from_training_files(path)
    features = dict.fromkeys(create_feature.create_boolean_feature_set(documents) )

    dr_bag_of_words = create_boolean_bag_of_words(features, documents.dr)
    dt_bag_of_words = create_boolean_bag_of_words(features, documents.dt)
    l_bag_of_words = create_boolean_bag_of_words(features, documents.l)

    dr_probability_bag_of_words = computing_probability_of_words_given_class(dr_bag_of_words, features)
    dt_probability_bag_of_words = computing_probability_of_words_given_class(dt_bag_of_words, features)
    l_probability_bag_of_words = computing_probability_of_words_given_class(l_bag_of_words, features)

    total_num_of_training_docs = len(dr_bag_of_words) + len(dt_bag_of_words) + len(l_bag_of_words)

    probability_of_dr = len(dr_bag_of_words)/ total_num_of_training_docs
    probability_of_dt = len(dt_bag_of_words)/ total_num_of_training_docs
    probability_of_l = len(l_bag_of_words) / total_num_of_training_docs

    test_docs = create_feature.get_documents_from_folder(os.path.join(path, 'TEST'))
    #print(test_docs.keys())
    results = {}
    for doc in test_docs:
        doc_given_class = [[compute_probablity_of_doc_given_class(test_docs[doc], dr_probability_bag_of_words), "DR"], [compute_probablity_of_doc_given_class(test_docs[doc], dt_probability_bag_of_words), "DT"], [compute_probablity_of_doc_given_class(test_docs[doc], l_probability_bag_of_words), "L"] ]
        results[doc] = max( doc_given_class)[1]
        #print(doc,results[doc])
    create_feature.accuracy_of_results(results, "data/test-results.txt")


def compute_probablity_of_doc_given_class(document_str, class_probabilties):
    #first fill the bag of words if needed
    bag_of_words = {}
    for word in class_probabilties.keys():
        bag_of_words[word] = word in document_str
    log_sum = 0
    for word, word_is_there in bag_of_words.items():
        if word_is_there:
            log_sum += math.log1p(class_probabilties[word])
        else:
            log_sum +=  math.log1p(1 - class_probabilties[word])
    return log_sum

def computing_probability_of_words_given_class(bag_of_words, features):
    #ASK IF WE SHOULD INCREASE NUM OF DOCS BY ONE
    num_of_docs = len(bag_of_words) + 1
    P_w_given_c = dict.fromkeys(features.keys(), 0)
    for doc in bag_of_words:
        for word in bag_of_words[doc]:
             if bag_of_words[doc][word]: P_w_given_c[word] += 1
    for word in P_w_given_c:
            P_w_given_c[word] = (P_w_given_c[word] + 1) / num_of_docs
    return P_w_given_c

"""Requires a dictionary of features, that is word pointing to something to be overwritter
and a dictionary of documents where the file name points to contents of the documents
It then copys the features dict, and fills it with true or false"""
def create_boolean_bag_of_words(features, documents):
    bag_of_words = {}
    for key in documents:
        bag_of_words[key] = features.copy()
        #Goes through feature words and marks if they are true or false
        for word in bag_of_words[key]:
            bag_of_words[key][word] = word in documents[key]
    return bag_of_words

def main(argv):
    print(argv)

if __name__ == '__main__':
    #featureCreator.create_navie_boolean_feature_set('data')
    """
    docDict = create_feature.create_naive_document_dictionaries_from_training_files('data')
    create_feature.get_frequency_from_training_documents(docDict)
    """
    #testing Comparing the two methods
    naive_bayes('data')
    """documents = create_feature.create_naive_document_dictionaries_from_training_files('data')
    features = create_feature.create_boolean_feature_set(documents)
    print(features, len(features))"""
    #main(sys.argv)
