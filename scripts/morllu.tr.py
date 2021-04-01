# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

# This script takes morphologically segmented words line-by-line for a given string as input and
# prints out words in morllu format.

# We used the tokenization script (adapted) and the Turkish morphological segmentation tool developed by Çağrı Çöltekin
# which can be found here:
# https://github.com/coltekin/TRmorph

words_segmented = sys.stdin.readlines()

# This decreases the number of analyses produced by the segmenter
cleared_words_segmented = list()

tokens = list()
for segmentation in words_segmented:
    # print(segmentation)
    pair = segmentation.split('\t')
    # This eliminates analyses that is less likely to occur
    if len(pair) > 1:
        if str(pair[0]) == str(pair[1]).replace('-', '').strip('\n') or \
                str(pair[0]) == str(pair[1]).replace('-', '').capitalize().strip('\n'):
            # This puts morphemes in separate lines ready for morllu format
            morpheme = segmentation.replace('\t', '\n').replace('-', '\n').split('\n')
            num_tokens = len(tokens) - 1
            # This checks if the current token is a new one and if not, removes the empty token preceding the morpheme
            # from the list so that later it can get the correct morpheme id.
            if cleared_words_segmented.__contains__(morpheme[0]) and tokens[num_tokens] == (morpheme[0]):
                cleared_words_segmented.reverse()
                cleared_words_segmented.remove('')
                cleared_words_segmented.reverse()
            for m in morpheme:
                cleared_words_segmented.append(m)
            tokens.append(pair[0])

# print(cleared_words_segmented)
cleared_words_segmented.pop()
column_titles = ('ID', 'MORPH', 'MORPHEME', 'TYPE', '?', 'LEVEL', 'LEIPZIG', 'UNIMORP', 'WALS', 'FEATURES')

element_id = 0
element_subid = 0
word_id = 1
elements_nmb = 0

morrlu_format = list()

copy_cleared_words_segmented = cleared_words_segmented
# This creates a dictionary in which every morpheme has a value for the related column in the format
for element in cleared_words_segmented:
    word_line_slots = defaultdict()
    elements_nmb += 1
    # This deals with the numbering for each morpheme and word for ID column
    if element == '':
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

        count = len(morrlu_format) - 1
        for word_line in morrlu_format:
            if morrlu_format[count]['MORPH'] != element.rstrip('\n') and not str(word_line['ID']).__contains__('.') and \
                    word_line['MORPH'] == element.rstrip('\n'):
                element_id = word_line['ID']
                element_subid = 1

    for title in column_titles:
        if title == 'ID':
            word_line_slots[title] = element_id

        elif title == 'MORPH' or title == 'MORPHEME':
            word_line_slots[title] = element.rstrip('\n')
            if not element_id.__contains__('.') and title == 'MORPHEME':
                word_line_slots[title] = '-'
        elif title == 'TYPE':
            if element_id.__contains__('.1'):
                word_line_slots[title] = 'ROOT'
            elif not element_id.__contains__('.'):
                word_line_slots[title] = '-'
            else:
                word_line_slots[title] = 'INFL'

        elif title == 'LEVEL' and element_id.__contains__('.'):
            subparts = element_id.split('.')
            word_line_slots[title] = int(subparts[1]) - 1
        else:
            word_line_slots[title] = '-'
    morrlu_format.append(word_line_slots)

# This turns the previous structure into a text format in order to provide it as an argument for
morrlu_format_txt = ''

for item in morrlu_format:
    word_line = ''
    for title in item.keys():
        word_line += str(item[title]) + '\t'

    word_line += '\n'
    morrlu_format_txt += word_line

sys.stdout.write(morrlu_format_txt)
