# -*- coding: utf-8 -*-
import sys
import re
from collections import defaultdict
from copy import deepcopy

regex_puncs = r'[^a-zA-Z0-9çşşğıüöÜÖÇŞĞİǩťṕḉǯžʒǮƷŽǨḈṔŤIӀ\- ]'

regexs_not_sentence_boundry = (r'[0-9]+\.',  # dates, numbers
                               r'\([^\)]*\.',  # inside_paranthesis
                               r'[\"\`\“][^\"\”\'\.]+[\.!]*[^\"\”\'\.]+[\"\`\“]',
                               r'\b[A-ZÜÖÇŞĞİǮƷŽǨḈṔŤII]+\.',  # abreviations
                               r'[\.\?!][ ]?[a-zçşşğıüöǩťṕḉǯžʒ]+',
                               r'[\.\?!][\”\'\"][ ]?[a-zçşşğıüöǩťṕḉǯžʒ,]+'
                               )

sentence = sys.stdin.readlines()
words_segmented = deepcopy(sentence)

'''
This creates three nested dictionaries for each tokenized element.  The innermost dictionary keeps items which are
defined as tuples of fields (listed as column_titles below) and their corresponding value for each token.
The second dictionary keeps items of dictionaries at the element level. It consists of word lines having
those tuples. It has a key for each token indicating its place in the element. The outermost dictionary at
last corresponds to each element with keys defined with a specific id number.

The original format has 10 fields but here there are eleven with one extra named 'DUMMY' that has new line
values for each word.  It is to be used for later when the defined structure below is turned into a text.
It separates each word line.
'''
column_titles = ('ID', 'MORPH', 'MORPHEME', 'TYPE', '?', 'LEVEL', 'LEIPZIG', 'UNIMORP', 'WALS', 'FEATURES')

element_id = 0
element_subid = 0
word_id = 1
elements_nmb = 0

morrlu_format = list()

for element in words_segmented:
    word_line_slots = defaultdict()
    elements_nmb += 1
    if element == '\n':
        word_id += 1
        element_subid = 0
        element_id = str(word_id)
        continue
    else:
        elements_nmb += 1
        element_id = str(word_id) + '.' + str(element_subid)
        if element_subid == 0:
            element_id = str(word_id)
        element_subid += 1
    for title in column_titles:
        if title == 'ID':
            word_line_slots[title] = element_id

        elif title == 'MORPH' or title == 'MORPHEME':
            word_line_slots[title] = element.rstrip('\n')

        else:
            word_line_slots[title] = '-'

    morrlu_format.append(word_line_slots)

'''
This turns the previous structure into a text format in order to provide it as an argument for
sys.stdout.write() function.
'''
morrlu_format_txt = ''
sent_id = 1

for item in morrlu_format:
    word_line = ''
    for title in item.keys():
        word_line += str(item[title]) + '\t'

    word_line += '\n'
    morrlu_format_txt += word_line

sys.stdout.write(morrlu_format_txt)
