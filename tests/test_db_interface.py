import pytest
from malayalam_morpheme_splitter import *

def test_morph_analysis_empty_string():
    assert morph_analysis('') == [], "Empty string should return an empty list"

def test_morph_analysis_single_word():
    assert morph_analysis('ആന') == [['ആന']], "Single word should be analyzed correctly"

def test_morph_analysis_sentence():
    result = morph_analysis('ആനയുടെ വൃക്ഷമായ')
    expected = [['ആന', 'ഉടെ'], ['വൃക്ഷം', 'ആയ']]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_morph_analysis_multiple_split():
    assert morph_analysis('മനുഷ്യന്മാരിലൂടെ') == [['മനുഷ്യൻ', 'മാർ', 'ഇൽ', 'ഊടെ']]

def test_db_entry_add_new_entry():
    try:
        db_entry({'ചിരിയായ': ['ചിരി', 'ആയ']})
    except:
        pass
    result = morph_analysis('ചിരിയായ')
    expected = [['ചിരി', 'ആയ']]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_db_entry_redundancy():
    with pytest.raises(ValueError, match="This entry would create redundancy"):
        db_entry({'ആനയെ': ['ആന', 'എ']})

def test_root_word_entry_redundancy():
    with pytest.raises(ValueError, match="This entry would create redundancy"):
        root_word_entry('ആന')

def test_db_entry_size():
    len1 = len(read_all_examples())
    db_entry({'കരുത്തില്ല' : ['കരുത്ത്', 'ഇല്ല'], 'കരുത്തോടെ' : ['കരുത്ത്', 'ഓടെ']})
    len2 = len(read_all_examples())
    assert len2 - len1 == 2

def test_read_all_examples_consistency():
    try:
        db_entry({'പുസ്തകമായ': ['പുസ്തകം', 'ആയ']})
    except:
        pass
    examples = read_all_examples()
    assert 'പുസ്തകമായ' in examples, "Expected 'പുസ്തകത്തിൻ്റെ' to be present in examples after db_entry"

def test_db_entry_invalid_format():
    with pytest.raises(ValueError, match="Invalid format: new_answer must be a list"):
        db_entry({'അഭിനന്ദനം': 'അഭിനന്ദനം'})

def test_root_word_entry_invalid_format():
    with pytest.raises(ValueError, match="Invalid entry"):
        root_word_entry('')

def test_db_entry_empty_input():
    with pytest.raises(ValueError, match="Input dictionary is empty"):
        db_entry({})
