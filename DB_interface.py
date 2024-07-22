#!/usr/bin/env python3
# filename: db_interface.py

import os
import re
import sys
from morph_examples import examples
from malayalam_words import root_word_lookup

def read_all_examples():
    with open('output.txt', mode='w', encoding='utf-8') as out:
        sort_list = list(examples.keys())
        for ex in sorted(sort_list):
            out.write(ex + '\t')
            out.write(' '.join(examples[ex]) + '\n')

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
    return [word, '*']

def morph_anal(root):
    wrd = ''
    analysed_word = []
    while root != wrd:
        wrd = root
        if wrd in root_word_lookup:
            root = wrd
        else:
            temp = find_morph(wrd)
            root = temp[0]
            analysed_word = [temp[1]] + analysed_word
    return [root] + analysed_word

def file_open(filename):
    os.system(f'notepad {filename}' if os.name == 'nt' else f'gedit {filename}')

def db_entry():
    with open('input.txt', 'w', encoding='utf-8') as inp:
        inp.write('*' * 25 + 'Enter the inputs here' + '*' * 25 + '\n(Format:<full word><tab><root><space><suffix>)\n')
    input('Enter the examples in the text file, and save it.')
    file_open('input.txt')
    
    with open('input.txt', 'r', encoding='utf-8') as inp:
        for ln in inp:
            word = ln.split('\t')[0]
            try:
                new_answer = ln.split('\t')[1].strip().split(' ')
            except Exception as e:
                print(f"Error parsing {ln}: {e}")
                pass
            analysed_word = morph_anal(word)
            if new_answer == analysed_word and word in examples:
                print(f"This entry ({word}) would create redundancy")
            else:
                examples[word] = new_answer
                try:
                    with open('morph_examples.py', 'w', encoding='utf-8') as db:
                        db.write("examples = {")
                        for k, v in examples.items():
                            db.write(f"'{k}' : {v},\n")
                        db.write("}")
                        print(f"Word{word} -> {new_answer} has been successfully added!")
                except:
                    pass

def _do_choice1():
    read_all_examples()
    file_open('output.txt')

def _do_choice2():
    input('Enter the word(with suffixes) in the file and save it.')
    file_open('input.txt')
    with open('input.txt', 'r', encoding='utf-8') as inp:
        actual_words = inp.readlines()
    analysed_words = []
    for actual_word in actual_words:
        actual_word = actual_word.strip()
        if actual_word != "":
            analysed_words.append([actual_word, morph_anal(actual_word)])
    with open('output.txt', 'w', encoding='utf-8') as out:
        for analyzed_word in analysed_words:
            out.write(analyzed_word[0] +  "→"  + ' '.join(analyzed_word[1]) + '\n')
    file_open('output.txt')
    
def normal_exec():
    choice = 0
    print("What do you want?\n\t1. View the whole database\n\t2. Check the morph-segmentation for an entry\n\t3. Add examples to DB\n\t4. Exit the program\n")
    
    while choice != 4:
        choice = int(input("Enter choice: "))
        if choice == 1:
            _do_choice1()
        elif choice == 2:
            _do_choice2()
        elif choice == 3:
            db_entry()
        elif choice == 4:
            pass
        else:
            print("Hey! What does that mean?!")
            print("Select a number from below\n\t1. View the whole database\n\t2. Check the morph-segmentation for an entry\n\t3. Add examples to DB\n\t4. Exit the program\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        choice = sys.argv[1]
        if choice == '1':
            _do_choice1()
        elif choice == '2':
            _do_choice2()
        elif choice == '3':
            db_entry()
        else:
            print("Hey! What does that mean?!")
    else:
        normal_exec()
