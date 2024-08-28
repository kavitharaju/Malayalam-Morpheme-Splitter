import re
import os
from data.morph_examples import examples
from data.malayalam_words import root_word_lookup



def read_all_examples():
    return examples



def find_morph(word):
    if not word:
        return [word, '']
    for w in examples:
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
    for word, new_answer in inp.items():
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








            