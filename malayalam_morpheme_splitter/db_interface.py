"""
This module handles morphological analysis for Malayalam words.
It provides functions for reading the database, splitting words,
and managing database entries for examples and root_word_lookup.
"""
import re
import os
import importlib.util

data_dir = os.path.join(os.path.expanduser("~"), ".mms_data")
examples_path = os.path.join(data_dir, "morph_examples.py")
root_word_lookup_path = os.path.join(data_dir, "malayalam_words.py")

def load_module(path):
    """Loads a Python module from a specified file path."""
    spec = importlib.util.spec_from_file_location("module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

examples_module = load_module(examples_path)
root_word_lookup_module = load_module(root_word_lookup_path)

def read_all_examples():
    """Returns the entire examples dictionary."""
    return examples_module.examples

def find_morph(word):
    """
    Finds the morphological components of a word.
    
    Args:
        word (str): The word to analyze.
    
    Returns:
        list: A list containing the root word and its suffix.
    """
    if not word:

        return [word]
    for w in examples_module.examples.keys():
        if re.match(f'.*{word}$', w):
            if len(examples_module.examples[w]) > 1:
                suffix = examples_module.examples[w][1]
            else:
                suffix = None
            index = len(w) - len(word)
            word = examples_module.examples[w][0][index:]
            return [word, suffix]
    if len(word) > 1:
        pre_part = word[0]
        word = word[1:]
        morph_list = find_morph(word)
        return [pre_part + morph_list[0]] + morph_list[1:]
    return [word, None]

def morph_analysis(sentence):
    """
    Performs morphological analysis on a given word.
    
    Args:
        sentence (str): The word or sentence to analyze.
    
    Returns:
        list: A list of lists containing the analysis of each part of the word or sentence.
    """
    words = re.findall(r'[\u0080-\uFFFF]+|\w+', sentence)
    analyzed_words = []
    for word in words:
        analyzed_word = []
        root = ''
        while word != root:
            root = word
            if word in root_word_lookup_module.root_word_lookup:
                analyzed_word.insert(0, word)
                break
            temp = find_morph(word)
            word = temp[0]
            if temp[1]:
                analyzed_word.insert(0, temp[1])
        if not analyzed_word or analyzed_word[0] != word:
            analyzed_word.insert(0, word)
        analyzed_words.append(analyzed_word)
    return analyzed_words

def db_entry(inp):
    """
    Adds entries in the examples database.
    
    Args:
        inp (dict): A dictionary where keys are words and 
        values are the analyzed forms inside a list.
    
    Raises:
        ValueError: If the input dictionary is empty or if the entry would create redundancy.
        FileNotFoundError: If the examples file is not found.
        PermissionError: If there's a permission issue when writing to the file.
        IOError: For other I/O related errors.
    """
    if not inp:
        raise ValueError("Input dictionary is empty")
    for word, new_answer in inp.items():
        entries = ''
        if not isinstance(new_answer, list):
            raise ValueError("Invalid format: new_answer must be a list")
        analysed_word = find_morph(word)
        if new_answer == analysed_word and word in examples_module.examples:
            raise ValueError('This entry would create redundancy')
        examples_module.examples[word] = new_answer
        entries += f"'{word}': {new_answer},\n"
        try:
            with open(examples_path, 'r+', encoding='utf-8') as db:
                db.seek(0, os.SEEK_END)
                pos = db.tell()
                while pos > 0:
                    pos -= 1
                    db.seek(pos, os.SEEK_SET)
                    if db.read(1) == '}':
                        break
                db.seek(pos - 1, os.SEEK_SET)
                db.write(entries)
                db.write("}")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Examples file not found: {examples_path}") from e
        except PermissionError as e:
            raise PermissionError(f"Permission denied when writing to examples file: "\
                                  f"{examples_path}") from e
        except IOError as e:
            raise IOError(f"Error writing to examples file: {e}") from e

def root_word_entry(word):
    """
    Adds a new root word to the root_word_lookup list.
    
    Args:
        word (str): The root word to add.
    
    Raises:
        ValueError: If the entry would create redundancy or if the input is invalid.
        FileNotFoundError: If the root word lookup file is not found.
        PermissionError: If there's a permission issue when writing to the file.
        IOError: For other I/O related errors.
    """
    if not word:
        raise ValueError("Invalid entry")
    if word in root_word_lookup_module.root_word_lookup:
        raise ValueError('This entry would create redundancy')
    root_word_lookup_module.root_word_lookup.append(word)
    try:
        with open(root_word_lookup_path, 'r+', encoding='utf-8') as f:
            f.seek(0, os.SEEK_END)
            pos = f.tell()
            while pos > 0:
                pos -= 1
                f.seek(pos, os.SEEK_SET)
                if f.read(1) == ']':
                    break
            f.seek(pos - 1, os.SEEK_SET)
            f.write(f'"{word}",\n')
            f.write(']')
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Root word lookup file not found: {root_word_lookup_path}") from e
    except PermissionError as e:
        raise PermissionError(f"Permission denied when writing to root word lookup file: "\
                              f"{root_word_lookup_path}") from e
    except IOError as e:
        raise IOError(f"Error writing to root word lookup file: {e}") from e
