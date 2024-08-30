"""
This module handles morphological analysis for Malayalam words.
It provides functions for reading the database, splitting words,
and managing database entries for examples and root_word_lookup.
"""
import re
import os
from malayalam_morpheme_splitter.data.morph_examples import examples
from malayalam_morpheme_splitter.data.malayalam_words import root_word_lookup


def read_all_examples():
    """Returns the entire examples dictionary."""
    return examples


def find_morph(word):
    """
    Finds the morphological components of a word.
    
    Args:
        word (str): The word to analyze.
    
    Returns:
        list: A list containing the root word and its suffix.
    """
    if not word:
        return [word, '']
    for w in examples.items():
        if re.match(f'.*{word}$', w):
            suffix = examples[w][1]
            index = len(w) - len(word)
            word = examples[w][0][index:]
            if suffix == '-':
                return [word, ""]
            return [word, suffix]
    if len(word) > 1:
        pre_part = word[0]
        word = word[1:]
        morph_list = find_morph(word)
        return [pre_part + morph_list[0]] + morph_list[1:]
    return [word]



def morph_analysis(sentence):
    """
    Performs morphological analysis on a given word.
    
    Args:
        word (str): The word or sentence to analyze.
    
    Returns:
        list: A list of lists containing the analysis of each part of the word or sentence.
    """
    words = re.findall(r'[\u0080-\uFFFF]+|\w+', sentence)
    analyzed_words = []
    for word in words:
        analyzed_word = []
        root = word
        while True:
            if root in root_word_lookup:
                analyzed_word.insert(0, root)
                break
            temp = find_morph(root)
            root = temp[0]
            analyzed_word.insert(0, temp[1])
        analyzed_words.append(analyzed_word)
    return analyzed_words




def db_entry(inp):
    """
    Adds entries in the examples database.
    
    Args:
        inp (dict): A dictionary where keys are words and values are the analyzed forms.
    
    Raises:
        ValueError: If the entry would create redundancy.
    """
    for word, new_answer in inp.items():
        if not isinstance(new_answer, list):
            raise ValueError("Invalid format: new_answer must be a list")
        analysed_word = find_morph(word)
        if new_answer == analysed_word and word in examples:
            raise ValueError('This entry would create redundancy')
        examples[word] = new_answer
        try:
            with open('data/morph_examples.py', 'r+', encoding='utf-8') as db:
                db.seek(0, os.SEEK_END)
                pos = db.tell()
                while pos > 0:
                    pos -= 1
                    db.seek(pos, os.SEEK_SET)
                    if db.read(1) == '}':
                        break
                db.seek(pos - 1, os.SEEK_SET)
                for word, new_answer in inp.items():
                    db.write(f"'{word}' : {new_answer},")
                db.write("\n}")
        except:
            pass


def root_word_entry(word):
    """
    Adds a new root word to the root_word_lookup list.
    
    Args:
        word (str): The root word to add.
    
    Raises:
        ValueError: If the entry would create redundancy.
    """
    if not word:
        raise ValueError("Invalid entry")
    if word in root_word_lookup:
        raise ValueError('This entry would create redundancy')
    root_word_lookup.append(word)
    try:
        with open('data/malayalam_words.py', 'r+', encoding='utf-8') as f:
            f.seek(0, os.SEEK_END)
            pos = f.tell()
            while pos > 0:
                pos -= 1
                f.seek(pos, os.SEEK_SET)
                if f.read(1) == ']':
                    break
            f.seek(pos - 1, os.SEEK_SET)
            f.write(f'"{word}",\n]')
    except:
        pass
