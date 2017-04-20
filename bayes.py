import create_feature as featureCreator
import sys

def naive_bayes(training_path):
    bag_of_words = featureCreator.create_navie_boolean_feature_set(training_path)


def main(argv):
    print(argv)

if __name__ == '__main__':
    featureCreator.create_navie_boolean_feature_set('data')
    #main(sys.argv)
