import create_feature
import sys
import os
import math
from collections import namedtuple, Counter
import time

documentTypes = namedtuple('documentTypes', ['dr', 'dt','l'])

def naive_bayes(documents, test_docs, drop_short=False, drop_stop_words=False, nomial_bag_of_words=False):
    features = dict.fromkeys(create_feature.create_boolean_feature_set(documents, drop_short, drop_stop_words) )
    #print("Lenthg: ", len(features), features.keys())
    if(nomial_bag_of_words):
        dr_probability_bag_of_words = computing_multinomial_probability_of_words_given_class(documents.dr, features)
        dt_probability_bag_of_words = computing_multinomial_probability_of_words_given_class(documents.dt, features)
        l_probability_bag_of_words = computing_multinomial_probability_of_words_given_class(documents.l, features)
    else:
        dr_probability_bag_of_words = computing_multivariate_probability_of_words_given_class(documents.dr, features)
        dt_probability_bag_of_words = computing_multivariate_probability_of_words_given_class(documents.dt, features)
        l_probability_bag_of_words = computing_multivariate_probability_of_words_given_class(documents.l, features)
    #print(dr_probability_bag_of_words)
    total_num_of_training_docs = len(dr_probability_bag_of_words) + len(dt_probability_bag_of_words) + len(l_probability_bag_of_words)

    probability_of_dr = len(dr_probability_bag_of_words)/ total_num_of_training_docs
    probability_of_dt = len(dr_probability_bag_of_words)/ total_num_of_training_docs
    probability_of_l = len(dr_probability_bag_of_words) / total_num_of_training_docs


    #print(test_docs.keys())
    results = {}
    for doc in test_docs:
        #makes a list of all the probability of the document begin a given class, and the classe's name
        doc_bag_of_words = compute_bag_of_words_for_document(test_docs[doc], features, nomial_bag_of_words)
        doc_given_class = [[compute_probablity_of_doc_given_class(doc_bag_of_words, dr_probability_bag_of_words, nomial_bag_of_words), "DR"], [compute_probablity_of_doc_given_class(doc_bag_of_words, dt_probability_bag_of_words, nomial_bag_of_words), "DT"], [compute_probablity_of_doc_given_class(doc_bag_of_words, l_probability_bag_of_words, nomial_bag_of_words), "L"] ]
        results[doc] = max( doc_given_class)[1]
        #print(doc,results[doc])
    #create_feature.accuracy_of_results(results, "data/test-results.txt", True)
    return results

def compute_bag_of_words_for_document(document_str, features, nomial_bag_of_words=False):
    bag_of_words = {}
    if nomial_bag_of_words:
        for word in features.keys():
            bag_of_words[word] = document_str.count(word)
    else:
        for word in features.keys():
            bag_of_words[word] = word in document_str
    return bag_of_words
def compute_probablity_of_doc_given_class(bag_of_words, class_probabilties, nomial_bag_of_words=False):
    #first fill the bag of words if needed
    if nomial_bag_of_words:
        log_sum = 0
        for word, word_count in bag_of_words.items():
            #if word count isn't there then it will multiply by 0, thus not add to the probability
            if word_count != 0:
                log_sum += math.log(class_probabilties[word])*word_count
    else:
        log_sum = 0
        for word, word_is_there in bag_of_words.items():
            if word_is_there:
                log_sum += math.log(class_probabilties[word])
            else:
                log_sum +=  math.log(1 - class_probabilties[word])
    return log_sum

def computing_multinomial_probability_of_words_given_class(documents, features):
    bag_of_words = create_nomial_bag_of_words(features, documents)
    total_words = 2
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
    num_of_docs = len(bag_of_words) + 2
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

    correctedDocs = create_feature.create_naive_document_dictionaries_from_training_files('autocorrect_data', is_data_preprocessed=True)
    correctedTestDocs = create_feature.get_documents_from_folder(os.path.join('autocorrect_data', 'TEST'), is_data_preprocessed=True)
    print("-----------------------------\nOn normal data.")
    naive_bayes(documents, test_docs)
    print("-----------------------------\nOn data with words less than 3 dropped")
    naive_bayes(documents, test_docs, True)
    print("-----------------------------\nOn data without stop words")
    naive_bayes(documents, test_docs, False, True)
    print("-----------------------------\nOn data without stop words and words less than 3 dropped")
    naive_bayes(documents, test_docs, True, True)
    #print("-----------------------------\nOn auto Corrected data.")
    #naive_bayes(correctedDocs, correctedTestDocs)
    """
    print("-----------------------------\nNomial normal data.")
    naive_bayes(documents, test_docs, nomial_bag_of_words=True)
    print("-----------------------------\nNomial data with words less than 3 dropped")
    naive_bayes(documents, test_docs, True, nomial_bag_of_words=True)
    print("-----------------------------\nNomial data without stop words")
    naive_bayes(documents, test_docs, False, True, nomial_bag_of_words=True)
    print("-----------------------------\nNomial data without stop words and words less than 3 dropped")
    naive_bayes(documents, test_docs, True, True, nomial_bag_of_words=True)
    print("--------------------------------------------------------------------------------------------------------\nAutoCorrected Data")
    naive_bayes(correctedDocs, correctedTestDocs)
    
    print("-----------------------------\nOn autocorrected")
    naive_bayes(correctedDocs, correctedTestDocs)
    #print("-----------------------------\nOn normal data with nomoil Data")
    #naive_bayes(documents, test_docs, nomial_bag_of_words=True)

    print("----------------------------------------------------------\n normal data.")
    #naive_bayes(documents, test_docs)
    print("----------------------------------------------------------\nOn normal data.")
    naive_bayes(documents, test_docs, nomial_bag_of_words=True)
    """
