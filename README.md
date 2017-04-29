### Authors: Kevin Harris, Joscha Oswald, Nazar Stelmakh, Daniel Maida
### Email: kevin_harris@wsu.edu, joscha.oswald@wsu.edu nazar.stelmakh@wsu.edu, daniel.maida@wsu.edu

### Description: The following program is a supervised learning implementation of classifying documents.
There are three different approaches we took in attempting to classify each document; (1) Intelli-Grep
(2) Naive Bayes and (3) Perceptron. Each one takes a different approach in how to classify the document

### Run/Compile:
The program has been tested to work and run on a Linux environment using Python 3.5.2

There is a main.py file that takes a directory path as an arguement. The contents of that
directory are ASSUMED to contain a DR, DT, L, and TEST directory along with one test-results.txt
file (e.g. bash$ python3 main.py ./data/ OR bash$ python3 main.py ./autocorrect_data/). This main.py
file runs all three different as the initial implementation as well as multiple other times with
the added "improvements". After the main completes, it writes to a file called output.txt
in the current directory that will a list of output in the form:

<Implementation_Description>,<Original File Name>.txt,<Classification>

### Things to Note:

1) If the user needs to run an individual strategy, perceptron.py and bayes.py take the same
arguements as the main.py listed above. grep.py MUST take the final test directory 
(e.g. python3 grep.py ./data/TEST/)

2) With our auto corrected improvement, due to the inefficiency of this method (3+ hr. runtime)
we have excluded that from the default improvements to run in main.py. We have included a directory
with the initial data autocorrect and you may simply give that as an arguement. It was too much
effort for too little reward to automate it.

### Archive:
data/.............................Data files to run training and Tests on
autocorrect_data/.................Directory holding autocorrected data files
grep.py...........................Main file that runs Intelli-Grep
bayes.py..........................Main file that runs Naive Bayes
perceptron.py.....................Main file that runs Perceptron
create_feature.py.................File that contains improvement methods
processing.py.....................File that contains processing methods
main.py...........................Main executable program
README.md.........................This file

