# SYSTEM DESCRIPTION

The morph analyser is a python program that can be used to obtain the morphological segmentation of words.
It is an example based approach.(I guess my method can be called so)
There will be some examples of morphological segmentation already stored in the system DB. When a new word comes, the system checks the DB for the most matching example it has. This matching is done by checking for the similar endings of words. Then the segmentation is done as per the most similar example's.

## DB_interface.py

This is the main program. To check the system, run it as 'python DB_interface' from terminal. It has methods defined to segment the compound word, add examples and view the whole example DB. These methods can be used in other programs where you need the segmentation to be done.
To understand the logic better go through the code and try some trial runs.
Imp hint:-Pattern matching done in the following way
	-Search for the words in examples that has ending as the whole word(the word to be segmented)
	-If not found, search with the word with its first(left most) letter stripped.
	 (ie, if ആനയുടെ is not found, then search for നയുടെ)
	-Repeat the second step until a match is found or the word is completely stripped off.

## input.txt & output.txt

The files for input and output interface. The DB_interface program is written as, to read the inputs from input.txt and write its outputs to output.txt. If the files didn't open automatically it should be opened in a text editor(gedit). While giving input word to segment, make sure that there is no unwanted lines or spaces.

## morph_examples.py

This file has the python dictionary 'examples' that has examples for morphological segmentations.
The compound word is the key and a list of the last(right most) suffix and remaining word segment is the value.
The file can be appended if we find that the system doesn't segment a word properly.
Appending, or adding examples, is to be done through program.(DB_interface has a method defined for it.)
While appending make sure only the minimal examples are given. Redendency should be avoided.

## uniCodeMap.py

This file has a python dictionary uniCode that has the unicode characters as keys and the hex code for it in the form of ASCII string as the value. This is for using while creating the example DB through program. This was automatically created through the program createMap.py. I've done it for characters within the Malayalam's range. With a slight modification it can be used to create a mapping for any language's unicode.
