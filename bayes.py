import create_feature
import sys

def naive_bayes(training_path):
    bag_of_words = create_feature.create_navie_boolean_feature_set(training_path)


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
    bag_of_words = create_feature.create_boolean_feature_set(documents)
    print(bag_of_words)
    print('lenght:', len(bag_of_words))
    print('OLD WAY')
    new_bag_of_words = create_feature.file_create_naive_boolean_feature_set('data')
    print(new_bag_of_words)
    print("length", len(new_bag_of_words))
    #main(sys.argv)
