import re
from morph_examples import examples
from malayalam_words import root_word_lookup


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
    for word, new_answer in inp.items():
        analysed_word = find_morph(word)
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






            