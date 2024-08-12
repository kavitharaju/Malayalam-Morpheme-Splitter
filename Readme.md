# malayalam_morpheme_splitter
An example based approach at seperating suffixes from Malayalam. Malayalam is rich in morphological variations and is highly agglutinative.

## System Description

malayalam_morpheme_splitter is a Python package designed to split suffixes from Malayalam words using an example-based approach. The system comes with a set of malayalam root words and rules(examples) for suffix splitting. But users have the provision to add more root words and rules to improve the system performance if they notice incorrect outputs.

## Installation
To install malayalam_morpheme_splitter, you can use pip:

    pip install -i https://test.pypi.org/simple/ malayalam-morpheme-splitter==1.0.2

## Usage

```python
import malayalam_morpheme_splitter as mms

word_list = mms.morph_analysis('അമ്മച്ചിയുടെ') # ['അമ്മച്ചി', 'ഉടെ']
word_list1 = mms.morph_analysis('a sentence') # output

mms.read_all_examples() # returns all the examples in the database

mms.db_entry({'കരുതലിൻ്റെ':['കരുതൽ', 'ഇൻ്റെ']}) # add a new root to DB
```

## Functions
read_all_examples() : Reads all the examples from the DB and returns them as a dictionary.

morph_analysis(word) : This function takes a string as input and returns a dictionary. Key in the dictionary would be the word from the input string, and its corresponding value would be a list of all possible segmentations of that word.

db_entry(inp) : This function takes a dictionary as input and adds it to the DB.






