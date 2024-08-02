import json
import re
from morph_examples import examples
from malayalam_words import root_word_lookup


def load_config_file():
    with open("config.json", 'r', encoding='utf-8') as f:
        user_data = json.load(f)
    return user_data


def read_all_examples():
    user_data = load_config_file()
    user_data.update(examples)
    return user_data



def find_morph(word):
    user_data = load_config_file()
    if not word:
        return [word, '']

    for w in user_data:
        if re.match(f'.*{word}$', w):
            suffix = user_data[w][1]
            index = len(w) - len(word)
            word = user_data[w][0][index:]
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
    actual_word = root
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
    return {actual_word: [root] + analysed_word}



def db_entry(inp):
    user_data = load_config_file()
    for word, new_answer in inp.items():
        analysed_word = find_morph(word)
        existing_words = list(user_data.keys())
        if new_answer == analysed_word and (word in examples or word in existing_words):
            print(f"This entry ({word}) would create redundancy")
        else:
            user_data[word] = new_answer
            with open('config.json', 'w', encoding= 'utf-8') as f:
                json.dump(user_data, f, indent=4, ensure_ascii=False)
                print(f"Data saved to config.json")






            