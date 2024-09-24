# malayalam_morpheme_splitter
An example based approach at seperating suffixes from Malayalam. Malayalam is rich in morphological variations and is highly agglutinative.

## System Description

malayalam_morpheme_splitter is a Python package designed to split suffixes from Malayalam words using an example-based approach. The system comes with a set of malayalam root words and rules(examples) for suffix splitting. But users have the provision to add more root words and rules to improve the system performance if they notice incorrect outputs.

## Installation
To install malayalam_morpheme_splitter, you can use pip:

    pip install malayalam-morpheme-splitter

## Usage

```python
import malayalam_morpheme_splitter as mms

word_list = mms.morph_analysis('കരുതലിൻ്റെ') # ['കരുതൽ', 'ഇൻ്റെ']
word_list1 = mms.morph_analysis('ആനയെ കാണാൻ വനത്തിലേക്ക് പോവുക') # [['ആന', 'എ'], ['കാണാൻ'], ['വനം', 'ഇൽ', 'ഏക്ക്'], ['പോവുക']]

mms.read_all_examples() # returns all the examples in the database

mms.db_entry({'കരുതലിൻ്റെ':['കരുതൽ', 'ഇൻ്റെ']}) # add a new entry to DB

mms.root_word_entry('നികൃഷ്ടം') # add a new root word to DB
```

## Functions

* morph_analysis(sentence) : This function takes a string as input and returns a list containing segmentations.

Users can control or change the behaviour of the morpheme splitter. If you notice a certain kind of word is not split correctly, or a whord that should not be split is split, those can be fixed by adding data to the system userself:

* read_all_examples() : Reads all the examples from the DB and returns them as a dictionary. This can be used to examine the current rules.

* db_entry(inp) : This function takes a dictionary as input and adds it to the DB. Adding a new example will let the system learn that pattern and treat similar words in the way it i split in the given example.

* root_word_entry(word) : This function take a string as input and adds it to DB. A word which you think shpuld not be split, can be added here.





