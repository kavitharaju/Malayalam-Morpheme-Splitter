# Malayalam-Morpheme-Splitter
An example based approach at seperating suffixes from Malayalam. Malayalam is rich in morphological varations and is highly agglutinative.

## System Description

The Malayalam Morpheme Splitter is a python program that can be used to obtain the morphological segmentation of words. There will be some examples of morphological segmentation already stored in the system DB. When a new word comes, the system checks the DB for the most matching example it has. This matching is done by checking for the similar endings of words. Then the segmentation is done as per the most similar example's.

## DB_interface.py
This is the main program. To check the system, run it as 'python DB_interface' from terminal. It has methods defined to segment the compound word, add examples and view the whole example DB. These methods can be used in other programs where you need the segmentation to be done.
To understand the logic better go through the code and try some trial runs.
Imp hint:-Pattern matching done in the following way
	-Search for the words in examples that has ending as the whole word(the word to be segmented)
	-If not found, search with the word with its first(left most) letter stripped.
	-Repeat the second step until a match is found or the word is completely stripped off.

    Functions
        - read_all_examples() : Reads all the examples from the DB and returns them as a dictionary.
        - morph_analysis(word) : This function takes a string as input and returns a dictionary. Key in the dictionary would be the word from the input string, and its corresponding value would be a list of all possible segmentations of that word.
        - db_entry(inp) : This function takes a dictionary as input and adds it to the DB.


## morph_examples.py
This file has the python dictionary 'examples' that has examples for morphological segmentations.
The compound word is the key and a list of the last(right most) suffix and remaining word segment is the value.
The file can be appended if we find that the system doesn't segment a word properly.
Appending, or adding examples, is to be done through program.(DB_interface has a method defined for it.)
While appending make sure only the minimal examples are given. Redendency should be avoided.

## malayalam_words.py
This file contains a Python dictionary named root_word_lookup. This dictionary stores a list of words commonly found in malayalam.
The DB_interface.py program uses this list to perform a preliminary check during the segmentation process. By comparing the input word against the root words, the system can potentially identify the root part of the word before analyzing the suffixes using the morph_examples.py data.  



