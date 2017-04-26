import create_feature
import sys
import os
import math
from collections import namedtuple, Counter

documentTypes = namedtuple('documentTypes', ['dr', 'dt','l'])

def naive_bayes(documents, test_docs, drop_short=False, drop_stop_words=False, nomial_bag_of_words=False):
    features = dict.fromkeys(create_feature.create_boolean_feature_set(documents, drop_short, drop_stop_words) )
    print(features)
    if(nomial_bag_of_words):
        dr_probability_bag_of_words = computing_multinomial_probability_of_words_given_class(documents.dr, features)
        dt_probability_bag_of_words = computing_multinomial_probability_of_words_given_class(documents.dt, features)
        l_probability_bag_of_words = computing_multinomial_probability_of_words_given_class(documents.l, features)
    else:
        dr_probability_bag_of_words = computing_multivariate_probability_of_words_given_class(documents.dr, features)
        dt_probability_bag_of_words = computing_multivariate_probability_of_words_given_class(documents.dt, features)
        l_probability_bag_of_words = computing_multivariate_probability_of_words_given_class(documents.l, features)
    print(dr_probability_bag_of_words)
    total_num_of_training_docs = len(dr_probability_bag_of_words) + len(dt_probability_bag_of_words) + len(l_probability_bag_of_words)
    """print("bag of words")
    print("DR\n",dr_probability_bag_of_words)
    print("DT\n",dt_probability_bag_of_words)
    print("L\n",l_probability_bag_of_words)"""
    probability_of_dr = len(dr_probability_bag_of_words)/ total_num_of_training_docs
    probability_of_dt = len(dr_probability_bag_of_words)/ total_num_of_training_docs
    probability_of_l = len(dr_probability_bag_of_words) / total_num_of_training_docs


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

def computing_multinomial_probability_of_words_given_class(documents, features):
    bag_of_words = create_nomial_bag_of_words(features, documents)
    total_words = 1
    P_w_given_c = dict.fromkeys(features.keys(), 0)
    for doc in bag_of_words:
        for word in bag_of_words[doc]:
            P_w_given_c[word] += bag_of_words[doc][word]
            total_words += bag_of_words[doc][word]
    for word in P_w_given_c:
            P_w_given_c[word] = (P_w_given_c[word] + 1) / total_words
    return P_w_given_c

def computing_multivariate_probability_of_words_given_class(documents, features):
    bag_of_words = create_boolean_bag_of_words(features, documents)
    num_of_docs = len(bag_of_words) + 1
    P_w_given_c = dict.fromkeys(features.keys(), 0)
    for doc in bag_of_words:
        for word in bag_of_words[doc]:
             if bag_of_words[doc][word]: P_w_given_c[word] += 1
    for word in P_w_given_c:
            P_w_given_c[word] = (P_w_given_c[word] + 1) / num_of_docs
    return P_w_given_c

""" Counts the occurances of words and stores it in bag_of_words"""
def create_nomial_bag_of_words(features, documents):
    bag_of_words = {}
    for key in documents:
        bag_of_words[key] = dict.fromkeys(features.keys(), 0)#initalizing the bag of words to 0
        #Goes through feature words and marks if they are true or false
        for word in bag_of_words[key]:
            bag_of_words[key][word] += documents[key].count(word)
    return bag_of_words
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
    documents = create_feature.create_naive_document_dictionaries_from_training_files('data')
    test_docs = create_feature.get_documents_from_folder(os.path.join('data', 'TEST'))
    print("-----------------------------\nOn normal data.")
    naive_bayes(documents, test_docs)
    print("-----------------------------\nOn normal data with nomoil Data")
    naive_bayes(documents, test_docs, nomial_bag_of_words=True)
    """
    print("-----------------------------\nOn data with words less than 3 dropped")
    naive_bayes(documents, test_docs, True)
    documents = create_feature.create_naive_document_dictionaries_from_training_files('data')
    features = create_feature.create_boolean_feature_set(documents)
    print(features, len(features))
    print("-----------------------------\nOn data without stop words")
    naive_bayes(documents, test_docs, False, True)"""
    #main(sys.argv)
