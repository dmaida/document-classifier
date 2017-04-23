import create_feature
import sys
from collections import namedtuple

documentTypes = namedtuple('documentTypes', ['dr', 'dt','l'])

def naive_bayes(training_path):
    documents = create_feature.create_naive_document_dictionaries_from_training_files('data')
    features = create_feature.create_boolean_feature_set(documents)
    dr_bag_of_words = create_boolean_bag_of_words(features, documents.dr)
    dt_bag_of_words = create_boolean_bag_of_words(features, documents.dt)
    l_bag_of_words = create_boolean_bag_of_words(features, documents.l)
    print(dr_bag_of_words['WA_Pacific_2008-06-23__03112971.txt'])


"""Requires a dictionary of features, that is word pointing to something to be overwritter
and a dictionary of documents where the file name points to contents of the documents
It then copys the features dict, and fills it with true or false"""
def create_boolean_bag_of_words(features, documents):
    bag_of_words = {}
    for key in documents:
        bag_of_words[key] = features.copy()
        #Goes through feature words and marks if they are true or false
        for word in bag_of_words[key]:
            bag_of_words[key] = word in documents[key]
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
    #main(sys.argv)
