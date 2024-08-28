import re
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



def morph_analysis(word):
    word = re.findall(r'[\u0080-\uFFFF]+|\w+', word)
    analysis = []
    for wrd in word:
        if wrd == '':
            pass
        else:
            if wrd in root_word_lookup:
                wrd_analysis = [wrd]
            else:
                temp = find_morph(wrd)
                wrd_analysis = temp
            analysis.append(wrd_analysis)
    return analysis




def db_entry(inp):
    for word, new_answer in inp.items():
        analysed_word = find_morph(word)
        if new_answer == analysed_word and word in examples:
            raise ValueError(f'This entry would create redundancy')
        examples[word] = new_answer
        try:
            with open('data/morph_examples.py', 'a', encoding = 'utf-8') as db:
                for k, v in examples.items():
                    db.append(f"'{k}' : {v},\n")
                db.append("}")
        except: 
            pass



def root_word_entry(word):
    if word in root_word_lookup:
        raise ValueError(f'This entry would create redundancy')
    root_word_lookup.append(word)
    try:
        with open('data/malayalam_words.py', 'w', encoding = 'utf-8') as f:
            f.write("root_word_lookup = [")
            for wrd in root_word_lookup:
                f.write(f'"{wrd}",\n')
            f.write("]")
    except:
        pass








            