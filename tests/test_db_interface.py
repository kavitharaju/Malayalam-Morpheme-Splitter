import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.append('C:\Users\glady\Documents\dev\BCS\MalMorphemeSplitter\Malayalam-Morpheme-Splitter\malayalam_morpheme_splitter')
# from malayalam_morpheme_splitter.DB_interface import read_all_examples, morph_analysis, db_entry, root_word_entry
from malayalam_morpheme_splitter import *


def test_morph_analysis_empty_string():
    assert morph_analysis('') == []

def test_morph_analysis_single_word():
    assert morph_analysis('ആന') == [['ആന']]

def test_morph_analysis_sentence():
    assert morph_analysis('ആനയുടെ വൃക്ഷമായ') == [['ആന', 'ഉടെ'], ['വൃക്ഷം', 'ആയ']]

def test_morph_analysis_multiple_split():
    assert morph_analysis('മനുഷ്യന്മാരിലൂടെ') == [['മനുഷ്യൻ', 'മാർ', 'ഇൽ', 'ഊടെ']]

def test_db_entry_add_new_entry():
    new_entry = {'ചിരിയിൽ': ['ചിരി', 'ഇൽ']}
    db_entry(new_entry)
    assert morph_analysis('ചിരിയിൽ') == [['ചിരി', 'ഇൽ']]

def test_db_entry_redundancy():
    with pytest.raises(ValueError):
        db_entry({'ആനയെ': ['ആന', 'എ']})

def test_root_word_entry_redundancy():
    with pytest.raises(ValueError):
        root_word_entry('ആന')

def test_db_entry_size():
    len1 = len(read_all_examples())
    db_entry({'മലയോടെ' : ['മല', 'ഓടെ'], 'മലയുടെ' : ['മല', 'ഉടെ']})
    len2 = len(read_all_examples())
    assert len2 - len1 == 2

def test_read_all_examples_consistency():
    db_entry({'പുസ്തകത്തിൻ്റെ': ['പുസ്തകം', 'ഇൻ്റെ']})
    examples = read_all_examples()
    assert 'പുസ്തകത്തിൻ്റെ' in examples, "Expected 'പുസ്തകത്തിൻ്റെ' to be present in examples after db_entry"

def test_db_entry_update_existing_entry():
    db_entry({'മടി': ['മടി', '-']})
    db_entry({'മടി': ['മടി']})
    assert morph_analysis('മടി') == [['മടി']]

def test_db_entry_invalid_format():
    with pytest.raises(ValueError):
        db_entry({'അഭിനന്ദനം': 'അഭിനന്ദനം'})

def test_root_word_entry_invalid_format():
    with pytest.raises(ValueError):
        root_word_entry('')
